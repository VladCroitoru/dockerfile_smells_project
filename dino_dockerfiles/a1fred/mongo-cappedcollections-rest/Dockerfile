FROM alpine:3.7
LABEL maintainer="demalf@gmail.com"

ENV MONGODB_CONNECTION_STRING mongodb://localhost:27017
ENV MONGODB_DB_NAME mongorest
EXPOSE 5000

RUN apk add --update --no-cache uwsgi-python3 gcc python3-dev musl-dev linux-headers make
WORKDIR /app
ADD ./ /app
RUN pip3 install -r requirements.txt

CMD [ "python3", "main.py" ]
