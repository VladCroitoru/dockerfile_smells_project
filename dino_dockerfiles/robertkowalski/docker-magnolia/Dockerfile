FROM ubuntu:trusty

MAINTAINER Robert Kowalski <rok@kowalski.gd>

ENV MAGNOLIA_CE_VERSION 5.5.1

RUN groupadd -r magnolia && useradd -d /opt/magnolia -g magnolia magnolia

RUN apt-get update -y && apt-get upgrade -y

RUN sudo apt-get install software-properties-common -y --no-install-recommends
# add Oracle JAVA 8
RUN sudo add-apt-repository ppa:webupd8team/java
# accept license
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | \
  sudo debconf-set-selections
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | \
  sudo debconf-set-selections

RUN apt-get update -y && apt-get install -y --no-install-recommends \
  oracle-java8-installer \
  oracle-java8-set-default

# Set the locale
RUN apt-get install -y locales
RUN locale-gen en_US.UTF-8
RUN /usr/sbin/update-locale LANG=en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# install git & curl for dev
RUN apt-get install -y --no-install-recommends \
  curl \
  git

# install node 6
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
RUN sudo apt-get install -y nodejs

# install mgnl
RUN npm i -g @magnolia/cli

# setup directories and permissions
RUN mkdir -p /opt/magnolia /opt/magnolia/light-modules \
  && chown -R magnolia:magnolia /opt/magnolia/

RUN cd /opt/magnolia \
  && mgnl jumpstart --magnolia-version=$MAGNOLIA_CE_VERSION --path=/opt/magnolia/light-modules

# setup supervisor
RUN apt-get -q -y install supervisor
RUN mkdir -p /var/log/supervisor

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# adjust file limits
RUN echo "magnolia   hard     nofile          500000" >> /etc/security/limits.conf

WORKDIR /opt/magnolia
EXPOSE 8080
VOLUME ["/opt/magnolia/light-modules"]

CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
