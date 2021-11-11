FROM python:2-alpine

WORKDIR /usr/src/app

RUN apk update && \
    apk upgrade && \
    apk add git

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python src/parser_test.py

EXPOSE 5000

ENV FLASK_DEBUG 1
ENV FLASK_APP src/service.py
CMD [ "flask", "run", "--host=0.0.0.0" ]