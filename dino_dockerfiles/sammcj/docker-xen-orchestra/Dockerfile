FROM debian:jessie

ENV DEBIAN_FRONTEND noninteractive

RUN useradd -d /app -r app && \
    mkdir -p /static /storage /app/conf && \
    chown -R app /static /storage /app

WORKDIR /app

# Install requirements as per https://github.com/vatesfr/xo/blob/master/doc/installation/manual_installation.md
RUN apt-get -qq update && \
    apt-get -qq install --no-install-recommends ca-certificates apt-transport-https curl \
      lsb-release python-all rlwrap redis-server libpng-dev git python-minimal supervisor && \
    apt-get autoremove -qq && apt-get clean && rm -rf /usr/share/doc /usr/share/man /var/log/* /tmp/*

RUN curl https://deb.nodesource.com/node/pool/main/n/nodejs/nodejs_0.10.36-1nodesource1~jessie1_amd64.deb \
        > node.deb && dpkg -i node.deb && rm node.deb

# Clone code
RUN git clone --depth=1 http://github.com/vatesfr/xo-server && \
    git clone --depth=1 http://github.com/vatesfr/xo-web && \
    rm -rf xo-server/.git xo-web/.git xo-server/sample.config.yaml

# Build dependancies then cleanup
RUN apt-get -qq install --no-install-recommends make gcc g++ && \
        npm install -g npm --unsafe-perm && \
        cd /app/xo-server && npm install --unsafe-perm && \
    cd /app/xo-web && npm install --unsafe-perm && \
    /app/xo-web/gulp --production && \
    rm -rf ~/.npm /tmp/* /var/log/* /app/xo-web/node_modules \
        /var/lib/apt/lists/* && npm cache clean && \
    apt-get purge -qq gcc g++ make && apt-get clean -qq && \
        apt-get autoremove -qq

# Add configuration
ADD sample.config.yaml /app/xo-server/.xo-server.yaml

# Setup Supervisor to manage the application process
COPY supervisord.conf /etc/supervisor/supervisord.conf

EXPOSE 8000

CMD ["/usr/bin/supervisord"]
