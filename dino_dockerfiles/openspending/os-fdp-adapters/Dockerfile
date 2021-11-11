FROM python:3.6-alpine

RUN apk add --update \
    python3 \
    git \
    libpq \
    wget \
    ca-certificates \
    python3-dev \
    build-base \
    libxml2-dev \
    libxslt-dev \
    libstdc++
RUN update-ca-certificates

RUN rm -rf /var/cache/apk/*

WORKDIR /app
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD . .

COPY docker/startup.sh /startup.sh

EXPOSE 8000

CMD  /startup.sh
