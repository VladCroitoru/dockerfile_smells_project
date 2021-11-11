FROM python:3-alpine

ENV REPOSITORY=https://github.com/glowdigitalmedia/docker-puller.git

RUN apk update && \
    apk add openssh git curl docker bash

RUN git clone $REPOSITORY

WORKDIR /docker-puller/dockerpuller/

RUN rm scripts/*

RUN pip install --no-cache-dir -r /docker-puller/requirements.txt

VOLUME /docker-puller/dockerpuller/scripts/

EXPOSE 8000

ENTRYPOINT ["sh", "-c"]
CMD ["exec python app.py"]