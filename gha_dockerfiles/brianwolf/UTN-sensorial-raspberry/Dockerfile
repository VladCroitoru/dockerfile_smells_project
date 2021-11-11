FROM python:3.9-alpine

ARG ARG_VERSION=local

ENV VERSION=${ARG_VERSION}
ENV HOST=0.0.0.0
ENV PORT=80
ENV SEND_BACKEND_URL="http://${HOST}:${PORT}/api/v1/mocks/backend/metrics"
ENV TZ America/Argentina/Buenos_Aires

WORKDIR /home/utn/sensorial

COPY . .

CMD gunicorn -b ${HOST}:${PORT} --reload app:app

RUN pip install -r requirements.txt --upgrade pip
