// use web framework components. (like http.server in python)
use axum::{
    routing::{get, post},    // method decorators for routing
    http::{StatusCode, header},       // HTTP status codes
    response::IntoResponse, // Response trait for converting to an HTTP response
    Json,                   // JSON response type helper
    Router,                 // Router type
};

use serde::{Deserialize, Serialize};
use tokio::fs;

// Handling network addresses and ports
use std::net::SocketAddr;

// Data structures
#[derive(Serialize, Deserialize)]
struct HealthResponse {
    status: String,
    message: String,
    port: u16,
}

#[derive(Deserialize)]
struct EchoRequest {
    message: String,
}

#[derive(Serialize)]
struct EchoResponse {
    echo: String,
}

// server the index.html file
async fn serve_html() -> impl IntoResponse {
    match fs::read_to_string("web/index.html").await {
        Ok(content) => (
            StatusCode::OK,
            [(header::CONTENT_TYPE, "text/html")],
            content,
        ).into_response(),
        Err(_) => (
            StatusCode::NOT_FOUND,
            "index.html not found",
        ).into_response(),
    }
}


// Health check endpoint with CORS
async fn health() -> impl IntoResponse {
    let response = HealthResponse {
        status: "ok".to_string(),
        message: "Rust server is running".to_string(),
        port: 3000,
    };

    (
        StatusCode::OK,
        [
            (header::CONTENT_TYPE, "application/json"),
            (header::ACCESS_CONTROL_ALLOW_ORIGIN, "*"),
        ],
        Json(response),
    )
}

// Echo endpoint
async fn echo(Json(payload): Json<EchoRequest>) -> impl IntoResponse {
    let response = EchoResponse {
        echo: payload.message,
    };

    (
        StatusCode::OK,
        [
            (header::CONTENT_TYPE, "application/json"),
            (header::ACCESS_CONTROL_ALLOW_ORIGIN, "*"),
        ],
        Json(response),
    )
}

// Serve CSS files
async fn serve_css(
    axum::extract::Path(filename): axum::extract::Path<String>,
) -> impl IntoResponse {
    let path = format!("web/css/{}", filename);

    match fs::read_to_string(&path).await {
        Ok(content) => (
            StatusCode::OK,
            [(header::CONTENT_TYPE, "text/css")],
            content,
        ).into_response(),
        Err(_) => (
            StatusCode::NOT_FOUND,
            format!("CSS file not found: {}", filename),
        ).into_response(),
    }
}

// Serve JavaScript files
async fn serve_js(
    axum::extract::Path(filename): axum::extract::Path<String>,
) -> impl IntoResponse {
    let path = format!("web/js/{}", filename);

    match fs::read_to_string(&path).await {
        Ok(content) => (
            StatusCode::OK,
            [(header::CONTENT_TYPE, "application/javascript")],
            content,
        ).into_response(),
        Err(_) => (
            StatusCode::NOT_FOUND,
            format!("JavaScript file not found: {}", filename),
        ).into_response(),
    }
}

// Serve static files from the 'web' directory
async fn serve_static(
    axum::extract::Path(filename): axum::extract::Path<String>,
) -> impl IntoResponse {
    let path = format!("web/{}", filename);

    match fs::read_to_string(&path).await {
        Ok(content) => {
            let content_type = if filename.ends_with(".js") {
                "application/javascript"
            } else if filename.ends_with(".css") {
                "text/css"
            } else {
                "text/plain"
            };

            (
                StatusCode::OK,
                [(header::CONTENT_TYPE, content_type)],
                content,
            ).into_response()
        },
        Err(_) => (
            StatusCode::NOT_FOUND,
            format!("File not found: {}", filename),
        ).into_response(),
    }
}

// main does 4 things
#[tokio::main] // main() async ~ similar to asyncio.run() in Python
async fn main() {
    // 1, create a router - like Flask's app.route() getting the endpoints
    let app = Router::new()
        .route("/", get(serve_html))
        .route("/health", get(health))
        .route("/api/echo", post(echo))
        .route("/web/:filename", get(serve_static))
        .route("/css/:filename", get(serve_css))
        .route("/js/:filename", get(serve_js));

    // 2. define address - Similar to ('', 8000) in Python
    let addr = SocketAddr::from(([127, 0, 0, 1], 8080));

    println!("🦀 Rust server running at http://localhost:{}", addr.port());
    println!("Press Ctrl+C to stop");

    // 3. create and bind the server and listen for incoming connections
    let listener = tokio::net::TcpListener::bind(addr).await.unwrap();

    // start the server
    axum::serve(listener, app).await.unwrap();
}