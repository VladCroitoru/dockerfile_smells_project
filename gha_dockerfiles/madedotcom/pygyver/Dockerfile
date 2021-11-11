ARG IMAGE_REGISTRY
ARG BASE_IMAGE_GIT_TAG
FROM ${IMAGE_REGISTRY}/py-base:${BASE_IMAGE_GIT_TAG:-snapshot}

ENV TERM=xterm-256color

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip3 install -r requirements.txt

# add utility to prevent tests starting until databases are ready
# as recommended: https://docs.docker.com/compose/startup-order/
#
# suggestion for future: include this dependency in the base image
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait

COPY pygyver src/pygyver
COPY tests src/tests

COPY entrypoint.sh /bin/entrypoint

ENTRYPOINT ["/bin/entrypoint"]
