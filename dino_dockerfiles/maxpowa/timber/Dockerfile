FROM python:alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk --update add --no-cache --virtual build-deps gcc python3-dev musl-dev && \
    apk --update add --no-cache postgresql-dev

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

RUN apk del build-deps

COPY . /usr/src/app

EXPOSE 8080
ENV PG_CONNECT=''

CMD [ "python", "./app.py" ]
