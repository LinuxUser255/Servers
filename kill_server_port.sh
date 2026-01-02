#!/usr/bin/env bash

# Find the process using port 8080
lsof -ti:8000 | xargs kill -9