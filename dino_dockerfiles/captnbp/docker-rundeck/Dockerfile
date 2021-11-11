FROM java:8

LABEL app=rundeck
LABEL version=2.8.2

ENV	DEBIAN_FRONTEND noninteractive
ENV	TZ="Europe/Paris"

ENV	VERSION=2.8.2-1

RUN echo $TZ > /etc/timezone 
RUN dpkg-reconfigure tzdata

ENTRYPOINT /run.sh

EXPOSE 4440

RUN apt-get update && apt-get install -yq openssh-client sudo uuid-runtime

# Add the install commands
ADD ./install.sh /


# Change Rundeck admin password from default
ENV RDPASS RDPASS

ENV MYHOST MYHOST

# From address when sending email
ENV MAILFROM MAILFROM

# Download Rundeck
ADD http://download.rundeck.org/deb/rundeck-${VERSION}-GA.deb /tmp/rundeck.deb

# Run the installation script
RUN /install.sh

ADD http://search.maven.org/remotecontent?filepath=com/hbakkum/rundeck/plugins/rundeck-hipchat-plugin/1.5.0/rundeck-hipchat-plugin-1.5.0.jar /var/lib/rundeck/libext/rundeck-hipchat-plugin-1.5.0.jar
ADD https://raw.githubusercontent.com/inokappa/rundeck-datadog_event-notification-plugin/master/DatadogEventNotification.groovy /var/lib/rundeck/libext/
ADD https://github.com/higanworks/rundeck-slack-incoming-webhook-plugin/releases/download/v0.6.dev/rundeck-slack-incoming-webhook-plugin-0.6.jar /var/lib/rundeck/libext/rundeck-slack-incoming-webhook-plugin-0.6.jar

VOLUME /var/lib/rundeck/data
VOLUME /var/lib/rundeck/var
VOLUME /var/lib/rundeck/logs
VOLUME /var/rundeck/projects
VOLUME /var/log/rundeck
VOLUME /var/lib/rundeck/.ssh

RUN chown rundeck /tmp/rundeck

ADD ./run.sh /
