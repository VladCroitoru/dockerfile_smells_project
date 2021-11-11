FROM python:3.8-buster

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["./docker-entrypoint.sh"]
