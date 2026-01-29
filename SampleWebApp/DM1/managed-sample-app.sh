#!/bin/bash
set -euo pipefail

APP_IMAGE="sampleapp-managed:1.0"
APP_NAME="sampleapp1"
APP_NET="sampleapp-net"
APP_VOL="sampleapp-logs"

# Clean build context
rm -rf tempdir
mkdir -p tempdir/templates tempdir/static tempdir/logs

# Copy files
cp sample_app.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

# Dockerfile with management features
cat > tempdir/Dockerfile <<'EOF'
FROM python:3.12-slim

LABEL app="sampleapp" \
      purpose="docker-management-experiment" \
      version="1.0"

RUN pip install --no-cache-dir flask

# Create non-root user
RUN useradd -m appuser

WORKDIR /home/myapp
COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY sample_app.py /home/myapp/
RUN mkdir -p /home/myapp/logs && chown -R appuser:appuser /home/myapp

ENV APP_LOG=/home/myapp/logs/access.log

EXPOSE 8080

# Healthcheck (uses python stdlib to hit the endpoint)
HEALTHCHECK --interval=10s --timeout=2s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/_health').read()"

USER appuser
CMD ["python3", "/home/myapp/sample_app.py"]
EOF

cd tempdir
docker build -t "${APP_IMAGE}" .

# Create network + volume if not exists
docker network inspect "${APP_NET}" >/dev/null 2>&1 || docker network create "${APP_NET}"
docker volume inspect "${APP_VOL}" >/dev/null 2>&1 || docker volume create "${APP_VOL}"

# Run with resource limits + restart policy + read-only rootfs (extra hardening)
docker rm -f "${APP_NAME}" >/dev/null 2>&1 || true
docker run -d \
  --name "${APP_NAME}" \
  --network "${APP_NET}" \
  -p 8080:8080 \
  --restart unless-stopped \
  --cpus="0.50" --memory="256m" \
  --read-only \
  -v "${APP_VOL}":/home/myapp/logs \
  "${APP_IMAGE}"

docker ps --filter "name=${APP_NAME}"