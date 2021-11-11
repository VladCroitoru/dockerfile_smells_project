FROM jenkins
USER root

# system update
RUN apt-get update

# locale
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

# timezone (Asia/Tokyo)
ENV TZ JST-9

# etc
ENV TERM xterm

# add tools to work.
RUN apt-get install -y vim less

# Install in jq command
RUN curl -o /usr/local/bin/jq -L https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 && chmod +x /usr/local/bin/jq

# Installin docker client
ENV DOCKER_CLIENT_VERSION=1.12.6 \
    DOCKER_API_VERSION=1.24
RUN curl -fsSL https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_CLIENT_VERSION}.tgz \
  | tar -xzC /usr/local/bin --strip=1 docker/docker

# python2 pip install
RUN apt-get install -y python-pip python-setuptools
RUN pip install setuptools --no-use-wheel --upgrade

# python3 install
RUN apt-get install -y python3 python3-pip
RUN apt-get -f install
RUN apt-get install -y libnss3-tools libnss3 libnss3-dbg libnss3-dev
RUN apt-get install -y libgconf2-4 libxss1
RUN apt-get install -y fonts-liberation libappindicator1 xdg-utils

# selenium install
RUN pip3 install selenium

# fabric install
RUN pip install fabric
