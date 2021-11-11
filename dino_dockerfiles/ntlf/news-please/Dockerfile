FROM python:3.7.0-alpine3.8

RUN apk add -U --no-cache curl git make gcc python-dev libffi-dev musl-dev libxml2-dev libxslt-dev openssl-dev zlib-dev jpeg-dev
RUN pip install pipenv

WORKDIR /app
COPY . .

RUN pipenv install

CMD ["pipenv", "run", "start"]