FROM python:3.9-alpine
EXPOSE 8000

ENV GUNICORN_CMD_ARGS --bind=0.0.0.0 --workers=2
ENV SECRET_KEY "override_this"
ENV DEBUG "False"
ENV SQLITE_PATH "/data/db.sqlite3"
ENV ADMIN_USERNAME "admin"
ENV ADMIN_PASSWORD "changeme"
ENV ADMIN_EMAIL "admin@change.me"

VOLUME [ "/data" ]

WORKDIR /usr/src/app

RUN apk --update --no-cache add postgresql-libs python3-dev musl-dev postgresql-dev gcc

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "./startup.sh" ]
