FROM robfischer1/docker-sabnzbd-base
MAINTAINER "Rob" <robfischer1@gmail.com>
VOLUME ["/config","/data"]
EXPOSE 8080 9090
CMD ["/usr/bin/SABnzbd","--config-file","/config","--console","--server", "0.0.0.0:8080"]