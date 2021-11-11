FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

ARG WEBHOOK_URL_SELF_SIGNED_CERT

ENV WEBHOOK_URL ${WEBHOOK_URL_SELF_SIGNED_CERT}

RUN openssl req -new -newkey rsa:4096 -days 3650 -nodes -x509 \
    -subj "/C=US/ST=Denial/L=Springfield/O=Dis/CN=${WEBHOOK_URL}" \
    -keyout private.key -out cert.pem

COPY . .

CMD ["python3", "src/main.py"]
