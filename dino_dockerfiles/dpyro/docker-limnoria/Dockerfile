FROM python:3.6-alpine

LABEL maintainer Sumant Manne <sumant.manne@gmail.com>
LABEL description Docker image for the Limnoria IRC bot

ENV LIMNORIA_VERSION master

RUN apk add --update git && \
    pip3 install -r https://raw.githubusercontent.com/dpyro/Limnoria/${LIMNORIA_VERSION}/requirements.txt && \
    pip3 install git+https://github.com/dpyro/Limnoria.git@${LIMNORIA_VERSION} --upgrade && \
    apk del git && \
    rm -rf /var/cache/apk/*

COPY ["start.sh", "/usr/local/bin/"]
RUN chmod u+x /usr/local/bin/start.sh

RUN adduser -S limnoria && \
    mkdir -p /data && \
    chown limnoria /data

USER limnoria

VOLUME ["/data"]
WORKDIR /data

CMD ["/usr/local/bin/start.sh"]

# ONBUILD ARG CONFIG_FOLDER=config
# ONBUILD ADD [CONFIG_FOLDER] .
