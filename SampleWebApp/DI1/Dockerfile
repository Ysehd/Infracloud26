FROM python:3.10-slim

ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_PROGRESS_BAR=off

WORKDIR /app

RUN pip install flask --no-input

COPY . /app

EXPOSE 8080

CMD ["python", "sample_app.py"]
