FROM ubuntu:14.04

RUN apt-get update \
  && apt-get install -y curl wget php5-cli php5-curl unzip sudo xz-utils git

#instalando composer
RUN curl -s https://getcomposer.org/installer | php \
  && mv composer.phar /usr/local/bin/composer \
  && chmod +x /usr/local/bin/composer

#instalando docker-compose
ARG compose_version=1.22.0
RUN curl -o /usr/local/bin/docker-compose -L "https://github.com/docker/compose/releases/download/${compose_version}/docker-compose-$(uname -s)-$(uname -m)" \
  && chmod +x /usr/local/bin/docker-compose

#instalando docker
RUN wget -qO- https://get.docker.com/ | sh \
 && usermod -aG docker $(whoami)

# Ferramentas NodeJS
RUN cd /opt && \
    wget https://nodejs.org/dist/v4.5.0/node-v4.5.0-linux-x64.tar.xz && \
    tar xf node-v4.5.0-linux-x64.tar.xz && \
    PATH=$PATH:/opt/node-v4.5.0-linux-x64/bin
    
RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash - \
  && apt-get install -y nodejs \
  && npm install -g yarn \
  && docker --version \
  && docker-compose --version \
  && composer --version
  
RUN composer global require hirak/prestissimo
