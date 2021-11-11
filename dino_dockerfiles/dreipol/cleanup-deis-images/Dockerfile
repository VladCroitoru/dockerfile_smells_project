FROM python:3.4
RUN curl -o /usr/bin/docker https://get.docker.com/builds/Linux/x86_64/docker-1.7.1 && chmod +x /usr/bin/docker

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

CMD ["python", "cleanup.py"]
