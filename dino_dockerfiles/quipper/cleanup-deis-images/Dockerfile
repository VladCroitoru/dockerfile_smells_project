FROM python:3.4-alpine
RUN apk -U add curl \
  && curl -o /usr/bin/docker https://get.docker.com/builds/Linux/x86_64/docker-1.8.3 \
  && chmod +x /usr/bin/docker \
  && mkdir -p /usr/src/app

WORKDIR /usr/src/app
COPY . /usr/src/app

CMD ["python", "cleanup.py"]
