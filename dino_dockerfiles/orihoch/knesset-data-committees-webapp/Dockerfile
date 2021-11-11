FROM python:3.6-alpine

RUN apk add --update libpq build-base python3-dev postgresql-dev
RUN pip install psycopg2

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 5050

ENV WORKERS 4
ENV PORT 5050

ENTRYPOINT ["sh"]
CMD ["-c", "gunicorn -w ${WORKERS} -b :${PORT} main:app"]
