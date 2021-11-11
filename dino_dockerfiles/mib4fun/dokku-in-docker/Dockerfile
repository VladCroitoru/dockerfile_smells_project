FROM ubuntu:trusty
MAINTAINER Jonas Svatos <lsde@lsde.org>

ENV DEBIAN_FRONTEND=noninteractive

ADD 99_norecommands /etc/apt/apt.conf.d/99_norecommands


RUN apt-get update && apt-get install -y wget git \ 
	openssh-server supervisor ca-certificates apt-transport-https 


RUN wget -nv -O - https://get.docker.com/ | sh
RUN wget -nv -O - https://packagecloud.io/gpg.key | apt-key add -
RUN echo "deb https://packagecloud.io/dokku/dokku/ubuntu/ trusty main" | tee /etc/apt/sources.list.d/dokku.list
RUN apt-get update -qq && apt-get install -y dokku aufs-tools 
RUN apt-get install -y linux-image-extra-$(uname -r)


RUN locale-gen en_US.UTF-8
RUN mkdir /var/run/sshd
RUN ln -sf /home/dokku/HOSTNAME /home/dokku/VHOST
# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 22 80 443
VOLUME ["/home/dokku"]

ADD start /start
RUN chmod 755 /start
CMD ["/start"]
