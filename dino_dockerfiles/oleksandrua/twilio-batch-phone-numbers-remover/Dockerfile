FROM alpine:3.5

WORKDIR /app

RUN apk add --update python3

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./src /app

CMD [ "python3", "./app.py" ]