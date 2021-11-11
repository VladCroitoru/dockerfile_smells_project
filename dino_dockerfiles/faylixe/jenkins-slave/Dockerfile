FROM openjdk:8-alpine
MAINTAINER Felix Voituret <felix.voituret@gmail.com>

EXPOSE 22
ENTRYPOINT ["/entrypoint.sh"]
RUN apk add --update bash git openssh wget tar shadow
RUN wget -O /tmp/docker.tgz https://get.docker.com/builds/Linux/x86_64/docker-17.05.0-ce.tgz
RUN tar -xvzf /tmp/docker.tgz -C /tmp
RUN cp /tmp/docker/docker /usr/local/bin/
RUN rm -Rf /tmp/* && rm -Rf /var/cache/apk/*
RUN mkdir /var/run/sshd
RUN mkdir /home/jenkins \
    && adduser -D -s /bin/bash jenkins \
    && echo "jenkins:jenkins" | chpasswd \
    && chown -R jenkins:jenkins /home/jenkins \
    && chown -R jenkins:jenkins /etc/ssh
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD ["/usr/sbin/sshd", "-D"]