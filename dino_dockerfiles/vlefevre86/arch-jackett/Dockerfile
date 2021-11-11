FROM binhex/arch-base:2015062300
MAINTAINER sdesbure

# additional files
##################

# add supervisor conf file for app
ADD *.conf /etc/supervisor/conf.d/

# add install bash script
ADD *.sh /root/

# install app
#############

# make executable and run bash scripts to install app
RUN chmod +x /root/*.sh && \
    /bin/bash /root/install.sh

# docker settings
#################

# map /config to host defined config path (used to store configuration from supervisor)
VOLUME /config

# map /opt/Jackett/.config/Jackett to host defined config path (used to store configuration from Jackett)
VOLUME /opt/Jackett/.config/Jackett

# expose port for http
EXPOSE 9117

# run supervisor
################

# run supervisor
CMD ["supervisord", "-c", "/etc/supervisor.conf", "-n"]
