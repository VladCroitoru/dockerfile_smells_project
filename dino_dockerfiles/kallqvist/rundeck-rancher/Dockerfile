FROM ubuntu

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -qq update && apt-get -qqy upgrade && apt-get -qqy install --no-install-recommends bash openjdk-8-jre-headless procps sudo openssh-client mysql-client curl git && apt-get clean
RUN curl -Lo /tmp/rundeck.deb http://dl.bintray.com/rundeck/rundeck-deb/rundeck-2.7.1-1-GA.deb
RUN curl -Lo /tmp/rundeck-cli.deb https://github.com/rundeck/rundeck-cli/releases/download/v0.1.19/rundeck-cli_0.1.19-1_all.deb
RUN dpkg -i /tmp/rundeck*.deb && rm /tmp/rundeck*.deb
RUN chown rundeck:rundeck /tmp/rundeck

# todo: ?
RUN mkdir -p /var/lib/rundeck/.ssh
RUN chown rundeck:rundeck /var/lib/rundeck/.ssh

# Remove default plugins
# RUN rm -R /var/lib/rundeck/libext/*
# RUN rm -R /var/lib/rundeck/exp/webapp/WEB-INF/rundeck/plugins/*

# Slack plugin
RUN curl -Lo /var/lib/rundeck/libext/rundeck-slack-incoming-webhook-plugin-0.6.jar https://github.com/higanworks/rundeck-slack-incoming-webhook-plugin/releases/download/v0.6.dev/rundeck-slack-incoming-webhook-plugin-0.6.jar

# Python dependencies
RUN apt-get update && apt-get install -y python python-pip zip

# J2 templating for runtime config
RUN pip install j2cli
ADD ./config-templates /config-templates

# Build rundeck plugins
ADD plugins-source /build
WORKDIR /build
RUN ./build-all.sh && rm -R /build
WORKDIR /

ADD ./docker-entrypoint.sh /docker-entrypoint.sh

# server url will be generated from protocol, host and port if missing
ENV RDECK_SERVER_URL ""
ENV RDECK_PROTOCOL http
ENV RDECK_HOST localhost
ENV RDECK_PORT 4440
ENV RDECK_ADMIN_USERNAME admin
ENV RDECK_ADMIN_PASSWORD admin
ENV DATABASE_URL jdbc:h2:file:/var/lib/rundeck/data/rundeckdb;MVCC=true;TRACE_LEVEL_FILE=4
ENV DATABASE_USER rundeck
ENV DATABASE_PASSWORD rundeck

# todo: ?
# todo: /var/lib/rundeck/.ssh
VOLUME ["/var/lib/rundeck/logs"]

EXPOSE 4440

ENTRYPOINT ["/docker-entrypoint.sh"]

# check docker-entrypoint.sh, we keep this empty and check for empty command in entrypoint to allow command overrides at runtime
CMD [""]
