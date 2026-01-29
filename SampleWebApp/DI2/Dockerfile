# Dockerfile voor examen (stabiele versie)
FROM python:3.8.18-slim-bullseye

# Systeemafhankelijkheden installeren die nodig zijn voor Python-packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Pip upgraden en Flask installeren
RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir flask==2.2.5

# Werkdirectory instellen in de container
WORKDIR /home/myapp

# Applicatiebestanden kopiëren naar de container
COPY myapp.py .
COPY templates templates
COPY static static

# Poort 8080 beschikbaar maken voor de applicatie
EXPOSE 8080

# Flask-applicatie starten
CMD ["python3", "myapp.py"]
