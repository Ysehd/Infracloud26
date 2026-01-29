#!/bin/bash

# Oude container stoppen en verwijderen (indien aanwezig)
docker rm -f eigencontainer 2>/dev/null

# Tijdelijke build-map verwijderen
rm -rf tempimage

# Controleren of het hoofdscript bestaat
if [ ! -f myapp.py ]; then
  echo "❌ myapp.py niet gevonden"
  exit 1
fi

# Benodigde mappen aanmaken voor de Docker build
mkdir -p tempimage/templates tempimage/static

# Applicatiebestanden kopiëren naar de tijdelijke build-map
cp myapp.py tempimage/
cp -r templates/* tempimage/templates/
cp -r static/* tempimage/static/

# Dockerfile automatisch aanmaken
cat <<EOF > tempimage/Dockerfile
FROM python:3.8-slim

# Pip-versiecontrole uitschakelen (snellere en schonere build)
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# Flask installeren
RUN python -m pip install --no-cache-dir --progress-bar off flask==2.2.5

# Werkdirectory instellen in de container
WORKDIR /home/myapp

# Applicatiebestanden kopiëren naar de container
COPY myapp.py .
COPY templates templates
COPY static static

# Poort 8080 beschikbaar maken
EXPOSE 8080

# Flask-applicatie starten
CMD ["python3", "myapp.py"]
EOF


# Naar de tijdelijke build-map gaan
cd tempimage || exit

# Docker image bouwen
docker build -t eigenimage .

# Container starten op poort 8080
docker run -d -p 8080:8080 --name eigencontainer eigenimage

# Actieve containers tonen
docker ps
