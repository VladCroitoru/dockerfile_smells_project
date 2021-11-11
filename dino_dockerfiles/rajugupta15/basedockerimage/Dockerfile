# This is the Dockerfile for basedockerimage contains sshd, supervisord, envtpl, consul-template
FROM ubuntu:14.04
MAINTAINER TheGeekLinux <rajugupta15@gmail.com>
ENV WORKHOME /usr/local/content
RUN mkdir /usr/local/content
ADD ./supervisor/sshd.conf /etc/supervisor/conf.d/sshd.conf
ADD ./scripts/ /scripts/base-image/
COPY ./config/init  /scripts/init
RUN echo "/bin/bash /scripts/base-image/start" >> /scripts/init && chmod a+x /scripts/init
ADD ./scripts/run.sh /usr/local/bin/run.sh
RUN chmod +x /usr/local/bin/run.sh
RUN bash /scripts/base-image/packages.sh 

# consul-template installation
RUN wget -P /tmp/ https://releases.hashicorp.com/consul-template/0.7.0/consul-template_0.7.0_linux_amd64.zip \
	&& unzip /tmp/consul-template_0.7.0_linux_amd64.zip -d /usr/local/bin/ && /bin/bash /scripts/base-image/cleanup.sh
EXPOSE 22
CMD ["/usr/local/bin/run.sh"]
