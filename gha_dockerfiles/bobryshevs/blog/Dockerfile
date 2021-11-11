
FROM python:3.9.7-alpine3.14
EXPOSE 9003
RUN apk add build-base
RUN apk add --no-cache \
        libressl-dev \
        musl-dev \
        libffi-dev 
WORKDIR /blog/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./.env ./.env
COPY . .
ENTRYPOINT python app.py 