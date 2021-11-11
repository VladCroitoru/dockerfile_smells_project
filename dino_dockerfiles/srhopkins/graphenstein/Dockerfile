FROM alpine:3.3
MAINTAINER Steven Hopkins <srhopkins@gmail.com>

RUN apk add --update python cairo supervisor

RUN apk add --update build-base python-dev py-pip cairo-dev libffi-dev git && \
    pip install cffi gunicorn graphite-api[sentry,cyanite] carbon whisper && \
    curl https://releases.hashicorp.com/consul/0.6.3/consul_0.6.3_linux_amd64.zip -o consul.zip && \
    curl https://releases.hashicorp.com/consul-template/0.13.0/consul-template_0.13.0_linux_amd64.zip -o consult.zip && \
    unzip -d /usr/bin consul.zip && unzip -d /usr/bin consult.zip && rm consul*.zip && \
    git clone https://github.com/grobian/carbon-c-relay.git && cd carbon-c-relay && make && \
    mv relay /usr/bin/carbon-c-relay && cd .. && rm -rf carbon-c-relay && \
    apk del build-base python-dev py-pip cairo-dev libffi-dev git

ADD supervisord.conf /etc/supervisord.conf
ADD carbon-c-relay.conf /etc/carbon-c-relay.conf

RUN mv /opt/graphite/conf/carbon.conf.example /opt/graphite/conf/carbon.conf
RUN mv /opt/graphite/conf/storage-schemas.conf.example /opt/graphite/conf/storage-schemas.conf
RUN sed -i 's/2003/2103/' /opt/graphite/conf/carbon.conf

RUN mkdir -p /srv/graphite
RUN ln -s /opt/graphite/storage/whisper /srv/graphite/whisper

CMD ["/usr/bin/supervisord"]
