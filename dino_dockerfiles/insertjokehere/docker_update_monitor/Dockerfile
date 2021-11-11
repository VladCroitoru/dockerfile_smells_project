FROM python:3.6

ARG DOCKER_VER=18.03.1-ce

RUN curl -L -o /tmp/docker-${DOCKER_VER}.tgz https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VER}.tgz \
    && tar -xz -C /tmp -f /tmp/docker-${DOCKER_VER}.tgz \
    && mv /tmp/docker/docker /usr/bin \
    && rm -rf /tmp/docker-${DOCKER_VER} /tmp/docker

WORKDIR /src

ADD requirements.txt /src/

RUN pip install -r /src/requirements.txt

ADD . /src/

ENTRYPOINT ["python", "__init__.py"]
