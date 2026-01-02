
# Servers: Python vs Rust HTTP Server Comparison

## 🎯 Purpose

This project is an educational exploration and practical comparison of building HTTP servers in two different programming languages: **Python** and **Rust**. The goal is to understand the trade-offs, performance characteristics, and development experience of each approach by implementing functionally equivalent servers.

## 🤔 Why This Project?

### Learning Objectives

1. **Language Comparison**: Understand the practical differences between Python and Rust for web server development
2. **Performance Analysis**: Measure and compare the performance characteristics of both implementations
3. **Development Experience**: Experience the different development workflows, from rapid Python prototyping to Rust's compile-time guarantees
4. **Translation Patterns**: Learn how to translate common web server patterns from Python to Rust
5. **Interoperability**: Explore options for integrating Python and Rust code

### Real-World Applications

- **Prototyping to Production**: Start with Python for rapid development, then migrate performance-critical parts to Rust
- **Microservices Architecture**: Use the right tool for each service (Python for ML/data, Rust for high-throughput APIs)
- **Performance Optimization**: Identify bottlenecks in Python and rewrite them in Rust
- **Team Skills**: Enable teams to work with both languages based on their strengths

## 📁 Project Structure
```text

Servers/
├── README.md                          # This file
├── main.py                            # Server orchestration and testing
├── server.py                          # Python HTTP server implementation
├── rust_server/                       # Rust server project
│   ├── Cargo.toml                     # Rust dependencies
│   ├── src/
│   │   └── main.rs                    # Rust HTTP server implementation
│   └── README.md                      # Rust-specific documentation
└── docs/
    ├── python_to_rust_translation.md  # Translation guide
    └── rust_server_instructions.md    # Setup instructions
```

## 🚀 Quick Start

### Prerequisites

**For Python Server:**
- Python 3.7+ (built-in modules only, no external dependencies)

**For Rust Server:**
- Rust 1.70+ ([Install Rust](https://rustup.rs/))
- Cargo (comes with Rust)

**For Testing:**
```bash
pip install requests
```
```bash
python main.py python
````

```bash
python main.py both
```

```bash
python main.py compare
```

## Server Implementations
Both servers implement the same REST API with identical endpoints:

## API Endpoints
```text

API Endpoints
| Method | Endpoint       | Description                    | Response                          |
|--------|----------------|--------------------------------|-----------------------------------|
| GET    | `/`            | Root endpoint                  | Plain text welcome message        |
| GET    | `/health`      | Health check                   | JSON status object                |
| POST   | `/api/create`  | Create a resource              | JSON with created resource info   |

```

## Example Requests
```bash
curl http://localhost:8000/health  # Python
curl http://localhost:3000/health  # Rust
```

## Create Resource:
```bash
curl -X POST http://localhost:8000/api/create \
  -H "Content-Type: application/json" \
  -d '{"name": "test"}'
 ```

<br>

# File: /Users/chris/Projects/Servers/README.md
# Servers: Python vs Rust HTTP Server Comparison

## 🎯 Purpose

This project is an educational exploration and practical comparison of building HTTP servers in two different programming languages: **Python** and **Rust**. The goal is to understand the trade-offs, performance characteristics, and development experience of each approach by implementing functionally equivalent servers.

## 🤔 Why This Project?

### Learning Objectives

1. **Language Comparison**: Understand the practical differences between Python and Rust for web server development
2. **Performance Analysis**: Measure and compare the performance characteristics of both implementations
3. **Development Experience**: Experience the different development workflows, from rapid Python prototyping to Rust's compile-time guarantees
4. **Translation Patterns**: Learn how to translate common web server patterns from Python to Rust
5. **Interoperability**: Explore options for integrating Python and Rust code

### Real-World Applications

- **Prototyping to Production**: Start with Python for rapid development, then migrate performance-critical parts to Rust
- **Microservices Architecture**: Use the right tool for each service (Python for ML/data, Rust for high-throughput APIs)
- **Performance Optimization**: Identify bottlenecks in Python and rewrite them in Rust
- **Team Skills**: Enable teams to work with both languages based on their strengths

## 📁 Project Structure

```
Servers/
├── README.md                          # This file
├── main.py                            # Server orchestration and testing
├── server.py                          # Python HTTP server implementation
├── rust_server/                       # Rust server project
│   ├── Cargo.toml                     # Rust dependencies
│   ├── src/
│   │   └── main.rs                    # Rust HTTP server implementation
│   └── README.md                      # Rust-specific documentation
└── docs/
    ├── python_to_rust_translation.md  # Translation guide
    └── rust_server_instructions.md    # Setup instructions
```

## 🚀 Quick Start

### Prerequisites

**For Python Server:**
- Python 3.7+ (built-in modules only, no external dependencies)

**For Rust Server:**
- Rust 1.70+ ([Install Rust](https://rustup.rs/))
- Cargo (comes with Rust)

**For Testing:**
```bash
pip install requests
```

### Running the Servers

**Start Python Server (Port 8000):**
```bash
python main.py python
```

**Start Rust Server (Port 3000):**
```bash
python main.py rust
```

**Start Both Servers Simultaneously:**
```bash
python main.py both
```

**Run A/B Comparison Tests:**
```bash
python main.py compare
```

## 🔍 Server Implementations

Both servers implement the same REST API with identical endpoints:

### API Endpoints

| Method | Endpoint       | Description                    | Response                          |
|--------|----------------|--------------------------------|-----------------------------------|
| GET    | `/`            | Root endpoint                  | Plain text welcome message        |
| GET    | `/health`      | Health check                   | JSON status object                |
| POST   | `/api/create`  | Create a resource              | JSON with created resource info   |

### Example Requests

**Health Check:**
```bash
curl http://localhost:8000/health  # Python
curl http://localhost:3000/health  # Rust
```

**Create Resource:**
```bash
curl -X POST http://localhost:8000/api/create \
  -H "Content-Type: application/json" \
  -d '{"name": "test"}'
```

## 📊 Comparison Matrix

### Python Server (`server.py`)

| Aspect              | Details                                      |
|---------------------|----------------------------------------------|
| **Framework**       | Built-in `http.server` module                |
| **Concurrency**     | Threading (ThreadingHTTPServer)              |
| **Port**            | 8000                                         |
| **Startup Time**    | ~Instant                                     |
| **Memory Usage**    | ~20-30 MB                                    |
| **Development**     | Rapid, dynamic typing                        |
| **Dependencies**    | None (standard library only)                 |
| **Best For**        | Prototyping, scripting, data processing      |

**Pros:**
- ✅ Extremely fast to develop and iterate
- ✅ No compilation step
- ✅ Easy to debug and modify
- ✅ Rich ecosystem for data science and ML
- ✅ Readable, concise code

**Cons:**
- ⚠️ Slower runtime performance
- ⚠️ GIL limits true parallelism
- ⚠️ Higher memory consumption
- ⚠️ Runtime errors (no compile-time checks)

### Rust Server (`rust_server/`)

| Aspect              | Details                                      |
|---------------------|----------------------------------------------|
| **Framework**       | Axum (modern async web framework)            |
| **Concurrency**     | Async/await with Tokio runtime               |
| **Port**            | 3000                                         |
| **Startup Time**    | ~2 seconds (compilation + runtime)           |
| **Memory Usage**    | ~5-10 MB                                     |
| **Development**     | Compile-time safety, static typing           |
| **Dependencies**    | Axum, Tokio, Serde                           |
| **Best For**        | High-performance APIs, system programming    |

**Pros:**
- ✅ Excellent runtime performance (10-100x faster)
- ✅ Memory safe without garbage collection
- ✅ True async concurrency (no GIL)
- ✅ Compile-time error catching
- ✅ Low memory footprint

**Cons:**
- ⚠️ Longer compilation time
- ⚠️ Steeper learning curve
- ⚠️ More verbose code
- ⚠️ Slower development iteration

## 🧪 Testing & Benchmarking

### Automated Testing

The `main.py` script provides comprehensive testing:

```bash
# Test Python server
python main.py test-python

# Test Rust server
python main.py test-rust

# Compare both servers
python main.py compare
```

### Manual Testing

**Python Server:**
```bash
# Terminal 1
python server.py

# Terminal 2
curl http://localhost:8000/health
```

**Rust Server:**
```bash
# Terminal 1
cd rust_server && cargo run

# Terminal 2
curl http://localhost:3000/health
```

### Performance Benchmarking

Use tools like `wrk` or `ab` (Apache Bench) for load testing:

```bash
# Install wrk (macOS)
brew install wrk

# Benchmark Python server
wrk -t4 -c100 -d30s http://localhost:8000/health

# Benchmark Rust server
wrk -t4 -c100 -d30s http://localhost:3000/health
```

## 🔄 Translation Guide

### Key Differences

**1. Request Handling**

*Python:*
```python
def do_GET(self):
    if self.path == '/health':
        response = {'status': 'ok'}
        self.wfile.write(json.dumps(response).encode())
```

*Rust:*
```rust
async fn health() -> Json<HealthResponse> {
    Json(HealthResponse {
        status: "ok".to_string(),
    })
}
```

**2. Type Safety**

*Python:* Dynamic typing, runtime errors
```python
def create(name):  # name could be anything
    return {'id': 1, 'name': name}
```

*Rust:* Static typing, compile-time checks
```rust
#[derive(Deserialize)]
struct CreateRequest {
    name: String,  // Must be a String
}
```

**3. Concurrency**

*Python:* Threading (limited by GIL)
```python
ThreadingHTTPServer(server_address, RequestHandler)
```

*Rust:* True async (no GIL)
```rust
#[tokio::main]
async fn main() {
    // Truly concurrent async operations
}
```

## 🔗 Python-Rust Interoperability

### Option 1: Separate Services (Recommended)

Run both servers independently and communicate via HTTP:

```
┌─────────────┐      HTTP      ┌──────────────┐
│   Rust      │ ◄─────────────► │   Python     │
│   Server    │                 │   Service    │
│  (Port 3000)│                 │  (Port 8000) │
└─────────────┘                 └──────────────┘
```

**Use Cases:**
- Rust handles high-throughput API requests
- Python handles ML inference, data processing
- Both communicate via REST API

### Option 2: PyO3 Integration

Embed Python in Rust or vice versa using [PyO3](https://pyo3.rs/):

```rust
use pyo3::prelude::*;

fn call_python() -> PyResult<()> {
    Python::with_gil(|py| {
        let sys = py.import("sys")?;
        let version: String = sys.getattr("version")?.extract()?;
        println!("Python version: {}", version);
        Ok(())
    })
}
```

**Use Cases:**
- Call Python ML models from Rust
- Use Python libraries in Rust applications
- Gradual migration from Python to Rust

### Option 3: Subprocess Communication

Run Python scripts from Rust:

```rust
use std::process::Command;

let output = Command::new("python3")
    .arg("script.py")
    .output()?;
```

## 📈 When to Use Each

### Choose Python When:
- 🚀 Rapid prototyping is priority
- 📊 Heavy data science/ML workloads
- 🔧 Frequent changes and iterations
- 👥 Team is primarily Python developers
- 📚 Rich ecosystem is needed (pandas, numpy, etc.)

### Choose Rust When:
- ⚡ Performance is critical
- 🔒 Memory safety is required
- 🌐 High concurrency is needed
- 📦 Low resource usage is important
- 🎯 Long-term stability is priority

### Use Both When:
- 🎨 Prototype in Python, optimize in Rust
- 🏗️ Microservices architecture
- 🔄 Different services have different needs
- 📊 Python for data, Rust for API

## 🎓 Learning Path

1. **Start Here**: Run both servers and compare their behavior
2. **Experiment**: Modify endpoints in both implementations
3. **Benchmark**: Test performance under load
4. **Translate**: Try converting Python code to Rust
5. **Integrate**: Experiment with PyO3 or HTTP communication
6. **Optimize**: Identify bottlenecks and optimize accordingly

## 📚 Additional Resources

### Python
- [Python http.server documentation](https://docs.python.org/3/library/http.server.html)
- [Threading in Python](https://docs.python.org/3/library/threading.html)

### Rust
- [The Rust Book](https://doc.rust-lang.org/book/)
- [Axum Documentation](https://docs.rs/axum/latest/axum/)
- [Tokio Tutorial](https://tokio.rs/tokio/tutorial)
- [PyO3 User Guide](https://pyo3.rs/)

### Web Development
- [HTTP Protocol](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [REST API Design](https://restfulapi.net/)

## 🤝 Contributing

This is an educational project. Feel free to:
- Add new endpoints to both servers
- Implement additional features (authentication, database, etc.)
- Add more comprehensive benchmarks
- Document your findings and learnings

## 📝 License

This project is for educational purposes. Use freely for learning and experimentation.

## 🎯 Next Steps

1. **Run the comparison**: `python main.py compare`
2. **Read the translation guide**: `docs/python_to_rust_translation.md`
3. **Experiment**: Modify both servers and observe differences
4. **Benchmark**: Test performance with real workloads
5. **Build**: Create your own hybrid Python-Rust application

---

**Happy Learning! 🚀**

*Explore the differences, understand the trade-offs, and choose the right tool for your needs.*
