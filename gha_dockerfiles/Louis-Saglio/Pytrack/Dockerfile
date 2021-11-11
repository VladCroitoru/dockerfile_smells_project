FROM python:3.9-slim-buster

WORKDIR /app

RUN pip install black

COPY ./test/test .
RUN chmod a-r /app/test

ENTRYPOINT ["/app/test"]
