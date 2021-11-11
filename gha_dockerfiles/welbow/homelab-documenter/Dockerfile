FROM python:3-alpine

WORKDIR /app
COPY . .

RUN apk add -U bash nmap &&\
    pip3 install -r requirements.txt --no-cache

ENTRYPOINT ["/usr/local/bin/python3", "/app/homelab-documenter.py"]
