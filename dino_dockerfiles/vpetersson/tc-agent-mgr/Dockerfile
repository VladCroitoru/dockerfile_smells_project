FROM python:3-alpine
WORKDIR /usr/src/app

RUN apk add --no-cache musl-dev libxml2-dev libxslt-dev python3-dev gcc

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py /usr/src/app
COPY settings.py /usr/src/app

USER nobody
CMD [ "python3", "./app.py"  ]
