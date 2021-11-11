FROM ubuntu:vivid

ENV LANG en_US.UTF-8
RUN locale-gen $LANG

RUN DEBIAN_FRONTEND=noninteractive apt-get update -q && apt-get install --no-install-recommends -q -y \
    ca-certificates \
    curl \
    software-properties-common \
    git-core \
    python2.7 \
    python-openssl \
    transmission-daemon \
    supervisor \
    nginx \ 
    unzip \
    unrar-free \
    par2

RUN DEBIAN_FRONTEND=noninteractive curl -s https://syncthing.net/release-key.txt | apt-key add - && \
    echo "deb http://apt.syncthing.net/ syncthing release" >> /etc/apt/sources.list && \
    add-apt-repository ppa:jcfp/ppa && \
    apt-get update && \
    apt-get install --no-install-recommends -q -y \
    syncthing \
    sabnzbdplus

RUN git clone https://github.com/rembo10/headphones.git /headphones

COPY config/supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY config/homepage /var/www/html
COPY config/nginx/default /etc/nginx/sites-available/default
COPY config/nginx/htpasswd /etc/nginx/conf.d/htpasswd
COPY config/sabnzbdplus/sabnzbdplus /etc/default/sabnzbdplus
COPY appdata/ /phono/appdata/
COPY start /start

VOLUME /phono/music
VOLUME /phono/appdata
VOLUME /etc/nginx/ssl

# Nginx
EXPOSE 80 443
# Syncthing discovery 
EXPOSE 22000 21025

ENTRYPOINT ["/start"]
