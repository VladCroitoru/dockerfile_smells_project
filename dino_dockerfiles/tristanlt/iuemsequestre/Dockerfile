# This DockerFile setup a fresh RabbitMQ container
# According to this simple configuration : http://tristan.lt/blog/rien-ne-sert-de-courrir-avec-rabbitmq/
#
FROM tristanlt/python27
MAINTAINER Tristan LT « me@tristan.lt »

ENV DEBIAN_FRONTEND noninteractive

RUN (apt-get update && apt-get upgrade -y -q && apt-get dist-upgrade -y -q && apt-get -y -q autoclean && apt-get -y -q autoremove)
RUN apt-get install -y -q supervisor python-imaging python-lxml python-ldap python-cjson libssl-dev libsasl2-dev libldap2-dev libgif-dev libjpeg62-dev libpng12-dev libfreetype6-dev libxml2-dev libxslt1-dev
RUN (cd /opt/ && git clone https://github.com/tristanlt/iuem.sequestre.git)
ADD supervisord.conf /etc/supervisor/conf.d/sequestre.conf
RUN adduser --system --disabled-password --shell /bin/bash --group --home /home/plone --gecos "Plone system user" plone
RUN chown -R plone.plone /opt/iuem.sequestre
RUN su plone -c "cd /opt/iuem.sequestre && /opt/BUILDOUT/buildout.python/python-2.7/bin/python bootstrap.py"
RUN su plone -c "cd /opt/iuem.sequestre && ./bin/buildout"
EXPOSE 8080
CMD ["/usr/bin/supervisord"]
