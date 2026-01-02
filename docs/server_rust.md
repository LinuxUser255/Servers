# Rust Server

```rust
use axum::{
    routing::{get, post},
    http::StatusCode,
    Json, Router,
};
use serde::{Deserialize, Serialize};
use std::net::SocketAddr;

#[derive(Serialize, Deserialize)]
struct HealthResponse {
    status: String,
    message: String,
}

#[derive(Deserialize)]
struct CreateRequest {
    name: String,
}

#[derive(Serialize)]
struct CreateResponse {
    id: u32,
    name: String,
    message: String,
}

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/", get(root))
        .route("/health", get(health))
        .route("/api/create", post(create_handler));

    let addr = SocketAddr::from(([127, 0, 0, 1], 3000));
    println!("🚀 Rust server listening on http://{}", addr);

    let listener = tokio::net::TcpListener::bind(addr).await.unwrap();
    axum::serve(listener, app).await.unwrap();
}

async fn root() -> &'static str {
    "Welcome to Rust Server!"
}

async fn health() -> Json<HealthResponse> {
    Json(HealthResponse {
        status: "ok".to_string(),
        message: "Server is running".to_string(),
    })
}

async fn create_handler(
    Json(payload): Json<CreateRequest>,
) -> (StatusCode, Json<CreateResponse>) {
    let response = CreateResponse {
        id: 1,
        name: payload.name,
        message: "Resource created successfully".to_string(),
    };

    (StatusCode::CREATED, Json(response))
}
```