#!/bin/bash
echo "DI2 container bouwen en starten..."

# Oude container stoppen en verwijderen
docker rm -f di2-running 2>/dev/null

# Temp build map leegmaken
rm -rf tempimage/*
mkdir -p tempimage

# Bestanden kopiëren
cp myapp.py tempimage/

# Dockerfile maken
cat <<EOF > tempimage/Dockerfile
FROM python:3.8-slim
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_PROGRESS_BAR=off
WORKDIR /home/myapp
RUN python -m pip install flask==2.2.5 --no-cache-dir --progress-bar off
COPY myapp.py .
EXPOSE 8080
CMD ["python3", "myapp.py"]
EOF

# Image bouwen
cd tempimage
docker build --no-cache -t di2-webapp .

# Container starten
docker run -d -p 8080:8080 --name di2-running di2-webapp
