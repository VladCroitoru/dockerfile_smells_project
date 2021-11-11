FROM ubuntu:xenial

WORKDIR /opt/

RUN apt-get update -y && apt-get install -y wget nginx supervisor && \
    apt-get install python-software-properties software-properties-common -y && \
    apt-add-repository ppa:bitcoin/bitcoin && apt-get update -y && \
    apt-get install -y bitcoind

# Tuning supervisor
RUN sed -i 's/^\(\[supervisord\]\)$/\1\nnodaemon=true/' /etc/supervisor/supervisord.conf

# Copy supervisor conf
COPY supervisor.conf /etc/supervisor/conf.d/programs.conf

# Add nginx config
ADD nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /root/.bitcoin && ln -s /etc/bitcoind/bitcoin.conf /root/.bitcoin/bitcoin.conf

EXPOSE 443
ENV PATH "/opt/bitcoind/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]
