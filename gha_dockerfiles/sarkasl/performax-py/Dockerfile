
FROM python:3.9.7-alpine
WORKDIR /app

ENV FLASK_APP=flask_app/app.py
ENV FLASK_ENV=production
ENV DATABASE_URL=postgresql://performax:JYvldxfLNqDI1gP@db:5432/performaxdb
ENV APPLICATION_SETTINGS=config.py
ENV SQL_HOST=db
ENV SQL_PORT=5432
ENV DATABASE=postgres

RUN apk add --no-cache gcc musl-dev linux-headers g++ postgresql-dev netcat-openbsd
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 80
COPY . .
CMD gunicorn --bind 0.0.0.0:80 run:app
ENTRYPOINT ["./entrypoint.sh"]  