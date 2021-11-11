# Docker image for Batoru-Royale
# Usage:
# Build the images

# docker pull redis
# docker pull rabbitmq
# docker pull elasticsearch

# docker build -t batoru-royale .

# Run the services

# docker run --name batoru-redis -d -P -p 6379:6379 redis
# docker run --name batoru-rabbitmq -d -P -p 5672:5672 rabbitmq
# docker run --name batoru-elasticsearch -d -P -p 9200:9200 elasticsearch

# docker run --name batoru-royale-socket --link batoru-redis:redis --link batoru-rabbitmq:rabbitmq --link batoru-elasticsearch:elasticsearch -p 5000:5000 -d -P batoru-royale python client.py
# docker run --name batoru-royale-read --link batoru-redis:redis --link batoru-rabbitmq:rabbitmq --link batoru-elasticsearch:elasticsearch -d batoru-royale python read.py

# docker run -it --rm --link batoru-redis:redis --link batoru-rabbitmq:rabbitmq --link batoru-elasticsearch:elasticsearch batoru-royale python simulate.py

FROM python:alpine

# Default port the webserver runs on
EXPOSE 5000

# Working directory for the application
WORKDIR /usr/src/app

# add certificates to talk to the internets
RUN apk add --no-cache ca-certificates

# Copy Python requirements so we only rebuild deps if they have changed
COPY requirements.txt /usr/src/app/

# Install all prerequisites (build base used for gcc of some python modules)
RUN apk add --no-cache build-base \
 && pip install --no-cache-dir -r requirements.txt \
 && apk del build-base

# Add the rest of the app code
COPY ./batoru /usr/src/app

RUN apk update
RUN apk add --no-cache sqlite

RUN python install.py
