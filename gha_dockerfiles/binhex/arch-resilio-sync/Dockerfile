FROM binhex/arch-base:latest
LABEL org.opencontainers.image.authors = "binhex"
LABEL org.opencontainers.image.source = "https://github.com/binhex/arch-resilio-sync"

# additional files
##################

# add supervisor conf file for app
ADD build/*.conf /etc/supervisor/conf.d/

# add install and packer bash script
ADD build/root/*.sh /root/

# get release tag name from build arg
ARG release_tag_name

# install app
#############

# make executable and run bash scripts to install app
RUN chmod +x /root/*.sh && \
	/bin/bash /root/install.sh "${release_tag_name}"

# docker settings
#################

# expose port for web ui
EXPOSE 8888

# expose port for incoming connection
EXPOSE 55555
EXPOSE 55555/udp

# set permissions
#################

# run script to set uid, gid and permissions
CMD ["/bin/bash", "/usr/local/bin/init.sh"]