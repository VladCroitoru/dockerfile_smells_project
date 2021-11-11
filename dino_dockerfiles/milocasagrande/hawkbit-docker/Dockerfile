FROM debian:jessie

MAINTAINER Milo Casagrande <milo.casagrande@linaro.org>
LABEL Version="1.0" Description="Run hawkbit in a docker container (or at least try)"

# Install mongodb from upstream repo.
# Use wheezy instead of jessie since jessie's version is systemd compatible
# but Docker vs Systemd is still an ongoing battle, and we need old style
# init script to be installed.
# Or better off using the official mongodb docker image and link it.
RUN echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.2 main" > \
    /etc/apt/sources.list.d/mongodb-org-3.2.list

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927

RUN apt-get update && apt-get install --no-install-recommends -y \
    sudo \
    git \
    mongodb-org \
    rabbitmq-server \
    && rm -rf /var/lib/mongodb \
    && mv /etc/mongod.conf /etc/mongod.conf.orig

COPY mongod.conf /etc/mongod.conf

RUN mkdir -p /data/db \
    && chown -R mongodb:mongodb /data/db

VOLUME /data/db

# Enable backports and install (more recent) packages from there.
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" > \
    /etc/apt/sources.list.d/jessie-backports.list

RUN apt-get update && apt-get install --no-install-recommends -y \
    -t jessie-backports \
    openjdk-8-jdk-headless \
    openjdk-8-jre-headless \
    maven \
    redis-server

# Clone and install hawkbit.
RUN cd /srv; git clone https://github.com/eclipse/hawkbit.git
# Use a custom pom.xml file where we add the mariadb dependency.
COPY pom.xml /srv/hawkbit/examples/hawkbit-example-app
RUN cd /srv/hawkbit; mvn clean install

COPY application.properties /srv

COPY ["start.sh", "hawkbit.sh", "/"]
RUN chmod +x /start.sh /hawkbit.sh
ENTRYPOINT ["/start.sh"]

EXPOSE 8080
CMD ["/hawkbit.sh"]
