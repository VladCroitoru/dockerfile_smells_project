FROM ubuntu:16.04
MAINTAINER Francis Levasseur <f.levasseur@tech-cl.com>
RUN DEBIAN_FRONTEND=noninteractive \
	apt-get update && \
	apt-get -y upgrade && \
	apt-get -y install nginx rsync cron

COPY nginx.conf /etc/nginx/sites-available/default
COPY mirror_ubuntu.sh /
COPY run.sh /

VOLUME /ubuntu_mirror
EXPOSE 80
CMD ["/run.sh"]
