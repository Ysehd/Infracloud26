#!/bin/bash

echo "🚀 DI1 Web App starten..."

# Oude container stoppen en verwijderen (indien bestaat)
docker rm -f di1-running 2>/dev/null

echo "🐳 Docker image bouwen..."
docker build -t di1-webapp .

echo "▶️ Container starten op poort 8080..."
docker run -d -p 8080:8080 --name di1-running di1-webapp

echo "✅ DI1 Web App draait op http://localhost:8080"
