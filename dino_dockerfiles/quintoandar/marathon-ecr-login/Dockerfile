FROM python:2-alpine

RUN apk update
RUN apk add --no-cache gcc linux-headers musl-dev

ADD . .

RUN pip install -r requirements.txt

CMD uwsgi --http :8000 -w app:app

EXPOSE 8000