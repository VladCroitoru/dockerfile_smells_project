FROM jenkins/jenkins:lts-alpine

USER root

RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.6/main' >> /etc/apk/repositories \
 && echo 'http://dl-cdn.alpinelinux.org/alpine/v3.6/community' >> /etc/apk/repositories

RUN addgroup -g 233 docker \
 && apk add --no-cache \
      docker \
      py2-pip \
      python \
      shadow \
      tzdata \
 && pip install --no-cache-dir \
      awscli \
      docker-compose \
 && usermod -a -G docker jenkins \
 && docker --version \
 && git --version \
 && aws --version \
 && git config --global user.email "jenkins@jenkins.com" \
 && git config --global user.name "Leroy Jenkins"

##Default Timezone - Can be overridden
ENV TZ=US/Central

COPY run-jenkins.sh /usr/local/bin/run-jenkins.sh
COPY s3-sync.sh /usr/local/bin/s3-sync.sh

ENTRYPOINT ["/sbin/tini", "--"]

CMD ["/usr/local/bin/run-jenkins.sh"]
