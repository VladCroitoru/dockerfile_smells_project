FROM alpine:3.6

LABEL maintainer="Anton Kvashenkin <anton.jugatsu@gmail.com> (@jugatsu)"

RUN apk --no-cache add python3 py3-pip

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt

COPY . /app/

WORKDIR /app/ui

ENV MONGO=mongo
ENV MONGO_PORT=27017
ENV FLASK_APP=ui.py

ENTRYPOINT ["gunicorn", "ui:app", "-b", "0.0.0.0"]
