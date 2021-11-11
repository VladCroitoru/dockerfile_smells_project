FROM ubuntu:xenial

WORKDIR /opt/

RUN apt-get update && apt-get install -y wget nginx supervisor && \
    wget https://download.litecoin.org/litecoin-0.13.2/linux/litecoin-0.13.2-x86_64-linux-gnu.tar.gz && \
    tar -zvxf litecoin-0.13.2-x86_64-linux-gnu.tar.gz && \
    mv litecoin-0.13.2 litecoin

# Tuning supervisor
RUN sed -i 's/^\(\[supervisord\]\)$/\1\nnodaemon=true/' /etc/supervisor/supervisord.conf

# Copy supervisor conf
COPY supervisor.conf /etc/supervisor/conf.d/programs.conf

# Add nginx config
ADD nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /root/.litecoin && ln -s /etc/litecoind/litecoin.conf /root/.litecoin/litecoin.conf

EXPOSE 443
ENV PATH "/opt/litecoin/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]