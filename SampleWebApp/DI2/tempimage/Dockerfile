FROM python:3.8-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

RUN python -m pip install --no-cache-dir --progress-bar off flask==2.2.5

WORKDIR /home/myapp
COPY myapp.py .
COPY templates templates
COPY static static

EXPOSE 8080
CMD ["python3", "myapp.py"]