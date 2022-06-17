# syntax=docker/dockerfile:latest
FROM python:3
COPY . /app
WORKDIR /app
# Mount cache for faster build
RUN --mount=type=cache,target=/root/.cache pip install -r requirements.txt
ENTRYPOINT python app.py