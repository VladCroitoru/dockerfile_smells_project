FROM python:3.8-slim-buster

RUN apt-get update && adduser --disabled-password --home /app api && update-ca-certificates && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD server.py .

EXPOSE 5000
USER api

ENTRYPOINT [ "/usr/local/bin/gunicorn" ]
CMD [ "-w", "4", "--bind", "0.0.0.0:5000", "server:app" ]