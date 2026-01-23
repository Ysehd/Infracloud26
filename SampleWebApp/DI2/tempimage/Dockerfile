FROM python:3.8-slim
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_PROGRESS_BAR=off
WORKDIR /home/myapp
RUN python -m pip install flask==2.2.5 --no-cache-dir --progress-bar off
COPY myapp.py .
EXPOSE 8080
CMD ["python3", "myapp.py"]
