FROM debian:jessie

RUN apt-get update -y && apt-get install --no-install-recommends -y -q curl python build-essential git ca-certificates
RUN mkdir /nodejs && curl http://nodejs.org/dist/v0.10.32/node-v0.10.32-linux-x64.tar.gz | tar xvzf - -C /nodejs --strip-components=1

ENV PATH $PATH:/nodejs/bin

RUN apt-get update && apt-get install -y \
    libfreetype6 libfreetype6-dev \
    libfontconfig1 libfontconfig1-dev \
    ruby ruby-dev locales libpng-dev
RUN echo "en_US UTF-8" >> /etc/locale.gen
RUN dpkg-reconfigure locales
RUN locale-gen en_US.UTF-8
RUN localedef -c -i en_US -f UTF-8 en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
RUN gem install sass compass
RUN npm install -g bower grunt-cli
RUN npm install -g npm
WORKDIR /app