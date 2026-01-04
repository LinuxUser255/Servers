// ============================================================================
// MINIMAL AXUM SERVER - BOILERPLATE
// ============================================================================

use axum::{
    routing::{get, post},
    Json,
    Router,
};
use serde::{Deserialize, Serialize};
use std::net::SocketAddr;

// ============================================================================
// DATA STRUCTURES
// ============================================================================

#[derive(Serialize)]
struct Message {
    message: String,
}

#[derive(Deserialize)]
struct EchoInput {
    text: String,
}

// ============================================================================
// HANDLERS
// ============================================================================

// GET /
async fn hello() -> &'static str {
    "Hello from Rust!"
}

// GET /health
async fn health() -> Json<Message> {
    Json(Message {
        message: "OK".to_string(),
    })
}

// POST /echo
async fn echo(Json(input): Json<EchoInput>) -> Json<Message> {
    Json(Message {
        message: input.text,
    })
}

// ============================================================================
// MAIN
// ============================================================================

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // 1. Build the router
    let app = Router::new()
        .route("/", get(hello))
        .route("/health", get(health))
        .route("/echo", post(echo));

    // 2. Set the address
    let addr = SocketAddr::from(([127, 0, 0, 1], 8080));
    println!("Server is running at http://localhost:8080");

    // 3. Start the server
    let listener = tokio::net::TcpListener::bind(addr).await?;
    axum::serve(listener, app).await?;

    Ok(())
}
