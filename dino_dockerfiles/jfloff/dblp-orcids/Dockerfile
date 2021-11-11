FROM jfloff/alpine-python:latest
LABEL maintainer="jfloff@inesc-id.pt"

# install lxml
RUN set -ex ;\
    apk add --update --no-cache \
            g++ \
            gcc \
            libxslt-dev \
            py-lxml\
            ;\
    rm /var/cache/apk/*

# copy just requirements so we cache this only despite any changes to parse.py or other files
COPY requirements.pip /tmp/
RUN pip --no-cache-dir install -r /tmp/requirements.pip

# add application
WORKDIR /home/dblp-orcids
COPY . /home/dblp-orcids
ENTRYPOINT [ "./parse.py" ]
CMD ["--out", "--orcid"]