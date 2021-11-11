FROM ubuntu:14.04

MAINTAINER Santiago Rodríguez <scollazo@gmail.com>

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y curl git-core libssl-dev g++ mongodb-server mongodb supervisor make

#Install nvm and node v0.8.25
RUN (cd /opt && git clone https://github.com/creationix/nvm.git nvm)
RUN (/bin/bash -c "cd /opt/nvm && source nvm.sh && nvm install v0.8.25")

#Set PATH
ENV PATH $PATH:/opt/nvm/v0.8.25/bin/

#Install ripple and dependencies
RUN (adduser --disabled-password --gecos '' ripple)

RUN (cd /opt && git clone https://github.com/uoregon-libraries/ripple ripple)
ADD create_default_admin.patch /opt/ripple/create_default_admin.patch
RUN (cd /opt/ripple && patch -p1 < create_default_admin.patch )
RUN (cd /opt/ripple && npm install)
RUN (cd /opt/ripple/plugins && git clone https://github.com/uoregon-libraries/ripple-heatmap.git heatmap)


ADD config.js /opt/ripple/
RUN (SECRET=$(< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-32};echo;) && sed -i "s/CHANGEME/$SECRET/g" /opt/ripple/config.js)



RUN (touch /var/log/ripple.log && chown ripple.ripple /var/log/ripple.log && chown ripple.ripple /opt/ripple/* -R)

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ADD run.sh /opt/
RUN chmod 755 /opt/run.sh

VOLUME /var/lib/mongodb
EXPOSE 8888

CMD [ "/opt/run.sh" ] 

