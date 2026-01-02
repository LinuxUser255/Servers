#!/usr/bin/env python3
"""
Main entry point for running Python or Rust HTTP servers.
Usage:
    python3 main.py python    - Run Python server (port 8000)
    python3 main.py rust      - Run Rust server (port 3000)
    python3 main.py both      - Run both servers simultaneously
    python3 main.py test      - Test both servers (they must be running)
"""

import subprocess
import sys
import time
import os


def run_python_server():
    """Run the Python server directly"""

    print("🐍 Starting Python server on port 8000...")
    print("Press Ctrl+C to stop\n")
    # import and run the Python server (server.py)
    from server import main as server_main
    server_main()


def run_rust_server():
    """Run the Rust server via cargo"""
    print("🦀 Starting Rust server on port 3000...")
    if not os.path.exists("target/debug/server_rust"):
        print("Error: Build the Rust server. The first time may take a while...")

        # creates a new process and runs the Cargo build tool
        build_result = subprocess.run(
            ["cargo", "build", "--bin", "server_rust"],
            capture_output=True,
            text=True,
        )

        if build_result.returncode != 0:
            print(f"Error building Rust server: {build_result.stderr}")
            sys.exit(1)
        print("Rust server built successfully!")

    print("Press Ctrl+C to stop\n")

    # Run the Rust server (target/debug/server_rust)
    try:
        subprocess.run(["cargo", "run", "--bin", "server_rust"])
    except KeyboardInterrupt:
        print("\n\nServer stopped.")


def print_usage():
    """Print the module's docstring."""
    print(__doc__)


def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    command = sys.argv[1].lower()

    try:
        if command == 'python':
            run_python_server()
        elif command == 'rust':
            run_rust_server() # calling the Rust server fucntion
        elif command in ['help', '-h', '--help']:
            print_usage()
        else:
            print(f"Invalid command: {command}")
            print_usage()
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n Server stopped.")
        sys.exit(0)


if __name__ == '__main__':
    main()
