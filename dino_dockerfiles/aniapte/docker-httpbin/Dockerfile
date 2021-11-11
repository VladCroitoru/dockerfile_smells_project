FROM python:3-alpine

RUN apk add -U ca-certificates libffi libstdc++ && \
    apk add --virtual build-deps build-base libffi-dev && \
    # Pip
    pip install --no-cache-dir gunicorn httpbin && \
    # Cleaning up
    apk del build-deps && \
    rm -rf /var/cache/apk/*

COPY cert.pem cert.pem
COPY key.pem key.pem

EXPOSE 443

CMD ["gunicorn", "--certfile", "cert.pem", "--keyfile", "key.pem", "-b", "0.0.0.0:443", "httpbin:app"]
