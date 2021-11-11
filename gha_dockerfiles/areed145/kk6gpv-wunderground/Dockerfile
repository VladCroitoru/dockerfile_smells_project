FROM python:3.7-slim-buster

LABEL maintainer="areed145@gmail.com"

WORKDIR /wunderground

COPY . /wunderground

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENV MONGODB_CLIENT 'mongodb+srv://kk6gpv:kk6gpv@cluster0.kglzh.azure.mongodb.net/test?retryWrites=true&w=majority'
ENV SID 'KTXMONTG307'
ENV API '931fd9ce91c240069fd9ce91c2c00690'

CMD ["python", "wunderground/wunderground.py"]
