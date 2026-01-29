FROM python:3.12-slim

RUN pip install flask
RUN useradd -m appuser

WORKDIR /home/myapp
COPY sample_app.py .

RUN mkdir -p /home/myapp/logs && chown -R appuser:appuser /home/myapp

ENV APP_LOG=/home/myapp/logs/access.log
EXPOSE 8080

USER appuser
CMD ["python3", "sample_app.py"]
