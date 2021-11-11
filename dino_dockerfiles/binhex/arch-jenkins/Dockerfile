FROM binhex/arch-base:latest
LABEL org.opencontainers.image.authors = "binhex"
LABEL org.opencontainers.image.source = "https://github.com/binhex/arch-jenkins"

# additional files
##################

# add supervisor conf file for app
ADD build/*.conf /etc/supervisor/conf.d/

# add install bash script
ADD build/root/*.sh /root/

# get release tag name from build arg
ARG release_tag_name

# add run bash script
ADD run/nobody/*.sh /home/nobody/

# install app
#############

# make executable and run bash scripts to install app
RUN chmod +x /root/*.sh /home/nobody/*.sh && \
	/bin/bash /root/install.sh "${release_tag_name}"

# docker settings
#################

# expose port for http
EXPOSE 8090

# expose port for docker api
EXPOSE 4243

# expose port for ssh
EXPOSE 22

# set environment variables for user nobody
ENV HOME /home/nobody

# set permissions
#################

# run script to set uid, gid and permissions
CMD ["/bin/bash", "/usr/local/bin/init.sh"]