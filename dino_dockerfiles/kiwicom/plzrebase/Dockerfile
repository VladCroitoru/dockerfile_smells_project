FROM python:3-alpine

WORKDIR /app

COPY requirements.txt /app
RUN apk --no-cache add --virtual=.run-deps git && \
    pip install -r requirements.txt

COPY . /app/
RUN pip install -e .

CMD ["plzrebase"]

LABEL name=plzrebase version=dev \
      maintainer="Simone Esposito <simone@kiwi.com>"

