FROM alpine:latest
MAINTAINER Pika Do <pokido99@gmail.com>

# Proxy settings if necessary
# ENV http_proxy=http://proxy:8080
# ENV https_proxy=http://proxy:8080
# ENV no_proxy="127.0.0.1,localhost,.mydomain.com"

# Upgrade system
RUN apk --no-cache upgrade

# Install Java
RUN apk --no-cache add openjdk7

# Install tools
RUN apk --no-cache add curl

# Install and configure JBoss AS
ENV JBOSS_VERSION 7.1.1.Final
ENV JBOSS_USER jboss
ENV JBOSS_HOME /usr/local/jboss-as
RUN curl -s -L http://download.jboss.org/jbossas/7.1/jboss-as-${JBOSS_VERSION}/jboss-as-${JBOSS_VERSION}.tar.gz | tar xz -C /usr/local && \
    ln -s /usr/local/jboss-as-${JBOSS_VERSION} ${JBOSS_HOME} && adduser -D -s /bin/sh ${JBOSS_USER} && chown -R ${JBOSS_USER}: /usr/local/jboss-as*
USER $JBOSS_USER
COPY run.sh /

# Set default command
CMD /run.sh
EXPOSE 8080 9990
