FROM python:3.8-alpine
WORKDIR /app
COPY . .
RUN apk add build-base
RUN apk add alpine-sdk
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install aiogram sqlalchemy psycopg2-binary
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["sh", "/app/entrypoint.sh" ]