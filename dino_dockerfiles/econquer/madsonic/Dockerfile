FROM java:latest
MAINTAINER econquer

# Install required packages
RUN apt-get update -q \
    && DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
	  supervisor curl nfs-common

ADD assets/install.sh /root/install.sh
RUN sh /root/install.sh

ADD assets/madsonic.conf /etc/supervisor/conf.d/
ADD assets/start.sh /opt/madsonic/start.sh
RUN chmod +x /opt/madsonic/start.sh

EXPOSE 4040

VOLUME ["/var/madsonic"]

CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]

