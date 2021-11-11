FROM debian:jessie

MAINTAINER Jookies LTD <jasmin@jookies.net>

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN groupadd -r jasmin && useradd -r -g jasmin jasmin

ENV JASMIN_VERSION 0.9b1

# Install requirements
RUN apt-get update && apt-get install -y \
    python2.7 \
    python-pip \
    python-dev \
    libffi-dev \
    libssl-dev \
    rabbitmq-server \
    redis-server \
    nano \
    joe \
    vim \
    lsb \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Install Jasmin SMS gateway
RUN mkdir -p /etc/jasmin/resource \
    /etc/jasmin/store \
    /var/log/jasmin \
  && chown jasmin:jasmin /etc/jasmin/store \
    /var/log/jasmin \
  && pip install redis \
  && pip install https://pypi.python.org/packages/py2.py3/p/pika/pika-0.10.0-py2.py3-none-any.whl \
  && pip install https://pypi.python.org/packages/source/t/txAMQP/txAMQP-0.6.2.tar.gz \
  && pip install --pre jasmin=="$JASMIN_VERSION" 

ENV GCSFUSE_REPO gcsfuse-jessie

RUN apt-get update && apt-get install --yes --no-install-recommends \
    ca-certificates \
    curl \
  && echo "deb http://packages.cloud.google.com/apt $GCSFUSE_REPO main" \
    | tee /etc/apt/sources.list.d/gcsfuse.list \
  && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - \
  && apt-get update \
  && apt-get install --yes gcsfuse \
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

# Change binding host for jcli
RUN sed -i '/\[jcli\]/a authentication=False' /etc/jasmin/jasmin.cfg
RUN sed -i '/\[jcli\]/a bind=0.0.0.0' /etc/jasmin/jasmin.cfg

EXPOSE 2775 8990 1401 5672 15672
VOLUME ["/var/log/jasmin", "/etc/jasmin", "/etc/jasmin/store"]

COPY config/configs.py /usr/local/lib/python2.7/dist-packages/jasmin/queues/
COPY config/clients.py /usr/local/lib/python2.7/dist-packages/jasmin/managers/
COPY config/pdu_encoding.py /usr/local/lib/python2.7/dist-packages/jasmin/vendor/smpp/pdu/
COPY config/factory.py /usr/local/lib/python2.7/dist-packages/jasmin/protocols/smpp/


COPY docker-entrypoint.sh /
RUN  chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["jasmind.py", "--enable-interceptor-client", "-u", "jcliadmin", "-p", "jclipwd"]
