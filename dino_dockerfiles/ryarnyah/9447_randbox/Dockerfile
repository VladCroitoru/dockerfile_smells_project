FROM debian:jessie

RUN apt-get update && \
    apt-get install -y python 

COPY . /src
WORKDIR /src

USER nobody
WORKDIR /src

EXPOSE 9447

ENTRYPOINT ["python", "randBox.py", "0.0.0.0", "9447"]
