FROM debian:jessie

MAINTAINER Julien BAYLE <julien.bayle@loire-atlantique.fr>

# WGET, NGNIX, VIM, ENVSUBST, QUILT, GIT
RUN apt-get update \
    && apt-get install -y vim gettext wget nginx-full quilt git \
    && rm -rf /var/lib/apt/lists/*

# APT SOURCES
RUN echo "deb http://httpredir.debian.org/debian/ jessie main" >> /etc/apt/sources.list \
    && echo "deb http://security.debian.org/debian-security jessie/updates main" >> /etc/apt/sources.list \
    && echo "deb http://ftp.fr.debian.org/debian jessie-updates main" >> /etc/apt/sources.list \
    && echo "deb http://ftp.fr.debian.org/debian jessie-backports main" >> /etc/apt/sources.list \
    && echo "deb http://deb.entrouvert.org/ jessie main" >> /etc/apt/sources.list \
    && wget -q -O- https://deb.entrouvert.org/entrouvert.gpg | apt-key add -

# BACKPORT PREFERENCES
COPY backports /etc/apt/preferences.d/backports

# DJANGO 1.8 (from backports)
RUN apt-get update \
    && apt-get install -y python-django \
    && rm -rf /var/lib/apt/lists/*

# TIMEZONE
RUN echo "Europe/Paris" > /etc/timezone && \
    apt-get update \
    && apt-get install -y locales \
    && rm -rf /var/lib/apt/lists/* \
    && dpkg-reconfigure -f noninteractive tzdata && \
    sed -i -e 's/# fr_FR.UTF-8 UTF-8/fr_FR.UTF-8 UTF-8/' /etc/locale.gen && \
    sed -i -e 's/# fr_FR.UTF-8 UTF-8/fr_FR.UTF-8 UTF-8/' /etc/locale.gen && \
    echo 'LANG="fr_FR.UTF-8"'>/etc/default/locale && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=fr_FR.UTF-8
ENV LANG fr_FR.UTF-8
ENV LANGUAGE fr_FR.UTF-8
ENV LC_ALL fr_FR.UTF-8

# THEME COMPILATION TOOLS (SASS & MAKEFILE support)
RUN apt-get update \
    && apt-get install -y build-essential ruby-sass \
    && rm -rf /var/lib/apt/lists/*

# INSTALL HOBO AGENT
# Always fails as it tries to connect to rabbitmq on configure phase
# So we modify package file to prevent hobo-agent from starting
# Todo this, these lines are removed from postinst script
#     supervisorctl reread
#     supervisorctl restart hobo-agent
RUN mkdir -p /etc/hobo-agent/settings.d 
COPY hobo-agent.settings.py /etc/hobo-agent/settings.d/broker.py
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       supervisor hobo-agent; exit 0
RUN sed -i '/supervisorctl/d' /var/lib/dpkg/info/hobo-agent.postinst \
    && apt-get install \
    && rm -rf /var/lib/apt/lists/*

# COPY GLOBAL PROPERTY FILES (COMMON TO ALL PUBLIK DOCKER COMPONENTS) 
COPY secret /tmp/secret
COPY global.nginx.conf /etc/nginx/conf.d/global.conf

# Add Wait-For-it COMAND LINE (DOCKER DEPENDENCIES MANAGEMENT MADE SIMPLE)
COPY wait-for-it.sh /root
RUN chmod +x /root/wait-for-it.sh

# Add PIP
RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py

# Add GRU UPDATE SCRIPT
COPY update.sh /root
COPY publik-prod-apt-preferences /etc/apt/preferences.d/
