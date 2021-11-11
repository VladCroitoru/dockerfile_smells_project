FROM debian:buster-slim
LABEL maintainer="Coding <code@ongoing.today>"

ENV DEBIAN_FRONTEND noninteractive
# Perl settings -n to don't to tests
ENV RT_FIX_DEPS_CMD /usr/bin/cpanm
ENV PERL_CPANM_OPT -n

SHELL ["/bin/bash", "-eo", "pipefail", "-c"]
RUN echo mail > /etc/hostname; \
    echo "postfix postfix/main_mailer_type string Internet site" > \
        preseed.txt && \
    echo "postfix postfix/mailname string mail.example.com" >> \
        preseed.txt && \
    debconf-set-selections preseed.txt && \
## Install tools and libraries
    apt update -yqq && \
    apt install -yqq --no-install-recommends \
        build-essential \
        ca-certificates \
        cpanminus \
        curl \
        elinks \
        git \
        gpgv2 \
        gnupg \
        graphviz \
        libexpat1-dev \
        libio-socket-ssl-perl \
        libpq-dev \
        libgd-dev \
        libssl-dev \
        lighttpd \
        openssl \
        perl \
        postfix \
        postgresql-client \
        ssl-cert \
        supervisor && \
# Create user and group
    groupadd -r rt-service && \
    useradd -r -g rt-service -G www-data rt-service && \
    usermod -a -G rt-service www-data && \
    mkdir -p /opt/rt5 && \
    chmod 0750 /opt/rt5 && \
    chown rt-service:www-data /opt/rt5 && \
    mkdir -p /tmp/rt && \
    curl -SL https://download.bestpractical.com/pub/rt/release/rt.tar.gz | \
        tar -xzC /tmp/rt && \
    cd /tmp/rt/rt* && \
    (echo y;echo o conf prerequisites_policy follow;echo o conf commit) | perl -MCPAN -e shell && \
    ./configure \
        --enable-graphviz \
        --enable-gd \
        --enable-gpg \
        --with-web-handler=fastcgi \
        --with-bin-owner=rt-service \
        --with-libs-owner=rt-service \
        --with-libs-group=www-data \
        --with-db-type=Pg \
        --with-web-user=www-data \
        --with-web-group=www-data \
        --prefix=/opt/rt5 \
        --with-rt-group=rt-service && \
    make fixdeps && \
    make testdeps && \
    make config-install dirs files-install fixperms instruct && \
    cpanm git://github.com/gbarr/perl-TimeDate.git && \
    cpanm RT::Extension::TerminalTheme && \
# Clean up
    apt remove -y git cpanminus build-essential && \
    apt-get autoremove -y && \
    apt-get clean && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /root/.cpan && \
    rm -rf /root/.cpanm && \
    rm -rf /preseed.txt /usr/share/doc && \
    rm -rf /tmp/rt && \
    rm -rf /usr/local/share/man /var/cache/debconf/*-old

# Copy files to docker
COPY entrypoint.sh /entrypoint.sh
COPY 89-rt.conf /etc/lighttpd/conf-available/89-rt.conf
COPY supervisord.conf /etc/supervisor/supervisord.conf

RUN chmod +x /entrypoint.sh && \
    sed -i '6 a ssl.ca-file = "/etc/lighttpd/server-chain.pem"' \
        /etc/lighttpd/conf-available/10-ssl.conf && \
    /usr/sbin/lighty-enable-mod rt && \
    /usr/sbin/lighty-enable-mod ssl && \
    chmod 770 /opt/rt5/etc && \
    chmod 660 /opt/rt5/etc/RT_SiteConfig.pm && \
    chown -R rt-service:www-data /opt/rt5/var && \
    chmod 0770 /opt/rt5/var

EXPOSE 443

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
