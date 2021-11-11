#
# Satis Dockerfile
#
# https://github.com/otternq/docker-satis
#

FROM dockerfile/nginx

MAINTAINER Nick Otter <otternq@gmail.com>

RUN \
  apt-get upgrade && \
  apt-get update -y && \
  apt-get install -y php5 php5-cli && \
  rm -rf /var/lib/apt/lists/*

ADD satis.json /opt/satis.json
ADD bootstrap-satis.sh /opt/bootstrap-satis.sh

RUN mkdir -p /opt/satis-stage && \
  (cd /opt/satis-stage && curl -sS https://getcomposer.org/installer | php) && \
  (cd /opt/satis-stage && php composer.phar create-project composer/satis --stability=dev --keep-vcs)

CMD ["/opt/bootstrap-satis.sh"]
