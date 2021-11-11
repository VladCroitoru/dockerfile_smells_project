FROM python:3.9

RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY bootstrap.sh .
COPY greenhat.py .

CMD ["./bootstrap.sh"]