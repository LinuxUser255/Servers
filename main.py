#!/usr/bin/env python3
"""
Main entry point for running Python or Rust HTTP servers.

Usage:
    python3 main.py python      - Run Python server (port 8000)
    python3 main.py rust        - Run Rust server (port 3000)
    python3 main.py rust_basic  - Run Basic Rust server (port 3000)
    python3 main.py help        - Show available commands
"""

import subprocess
import sys
import os


def run_python_server():
    """Run the Python server directly."""
    print("🐍 Starting Python server on port 8000...")
    print("Press Ctrl+C to stop\n")
    from server import main as server_main
    server_main()


def run_rust_server():
    """Run the Rust server via cargo."""
    print("🦀 Starting Rust server on port 3000...")

    if not os.path.exists("target/debug/server_rust"):
        print("Building Rust server. The first time may take a while...")
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

    try:
        subprocess.run(["cargo", "run", "--bin", "server_rust"])
    except KeyboardInterrupt:
        print("\n\nServer stopped.")


def run_rust_basic_server():
    """Run the Basic Rust server via cargo."""
    print("🦀 Starting Basic Rust server on port 3000...")

    if not os.path.exists("target/debug/server_rust_basic"):
        print("Building Basic Rust server. The first time may take a while...")
        build_result = subprocess.run(
            ["cargo", "build", "--bin", "server_rust_basic"],
            capture_output=True,
            text=True,
        )
        if build_result.returncode != 0:
            print(f"Error building Basic Rust server: {build_result.stderr}")
            sys.exit(1)
        print("Basic Rust server built successfully!")

    print("Press Ctrl+C to stop\n")

    try:
        subprocess.run(["cargo", "run", "--bin", "server_rust_basic"])
    except KeyboardInterrupt:
        print("\n\nServer stopped.")


# Command registry - add new commands here
COMMANDS = {
    "python": {
        "handler": run_python_server,
        "description": "Start the Python server (port 8000)",
    },
    "rust": {
        "handler": run_rust_server,
        "description": "Start the Rust server (port 3000)",
    },
    "rust_basic": {
        "handler": run_rust_basic_server,
        "description": "Start the Basic Rust server (port 3000)",
    },
    # Add new commands here:
    # "node": {
    #     "handler": run_node_server,
    #     "description": "Start the Node.js server",
    # },
}

HELP_ALIASES = {"help", "-h", "--help"}


def print_usage():
    """Print available commands and usage information."""
    print(__doc__)
    print("Available commands:")
    for cmd, info in COMMANDS.items():
        print(f"  {cmd:<12} {info['description']}")
    print(f"  {'help':<12} Show this help message")


def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    command = sys.argv[1].lower()

    try:
        if command in HELP_ALIASES:
            print_usage()
            sys.exit(0)

        if command in COMMANDS:
            COMMANDS[command]["handler"]()
        else:
            print(f"Invalid command: {command}")
            print_usage()
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n\nServer stopped.")
        sys.exit(0)


if __name__ == "__main__":
    main()
