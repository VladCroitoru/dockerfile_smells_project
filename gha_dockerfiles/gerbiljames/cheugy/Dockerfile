# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-alpine

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN apk add --update --no-cache ffmpeg gcc openssl-dev libffi-dev musl-dev make libsodium-dev opus-dev
RUN pip install --no-cache-dir -r requirements.txt

CMD exec python main.py