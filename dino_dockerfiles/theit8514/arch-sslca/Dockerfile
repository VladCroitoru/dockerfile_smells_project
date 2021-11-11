FROM jbbodart/arch-base
MAINTAINER theit8514

# setup easy-rsa
################

ENV EASY_RSA_VERSION 3.0.1

# dependencies
##############

ADD deps.sh /root/
RUN chmod +x /root/deps.sh && \
	/bin/bash /root/deps.sh && \
	rm -f /root/deps.sh

# base files
############

ENV PATH /easy-rsa:$PATH
ENV HOME /root

ADD supervisor/*.conf /etc/supervisor.d/
ADD nginx/nginx.conf /etc/nginx/nginx.conf

ADD install.sh /root/
RUN chmod +x /root/install.sh && \
	/bin/bash /root/install.sh && \
	rm -f /root/install.sh

ADD app/* /root/
RUN chmod +x /root/*.sh

# docker settings
#################

# map /data to host defined data path (used to store data from app)
VOLUME /data
# map /config to host defined config path (used to store config from app)
VOLUME /config

# expose port for nginx
EXPOSE 80
# expose port for OpenSSH server
EXPOSE 2222

# run supervisor
###########

WORKDIR /data

ENTRYPOINT ["/root/start.sh"]

# run supervisor
CMD ["supervisord", "-c", "/etc/supervisord.conf", "-n"]
