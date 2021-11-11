FROM python:3.8-slim-buster as production

# dont forget to map source to /app volume

#RUN apt-get -y update
#RUN apt-get -y install pkg-config libsecp256k1-dev

WORKDIR /app
ADD ./app/requirements.txt .

RUN apt-get update -y && \
    apt-get install build-essential cmake pkg-config -y

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py", "/config/config.yaml" ]