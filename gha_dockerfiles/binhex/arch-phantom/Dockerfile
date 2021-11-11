FROM binhex/arch-base:latest
LABEL org.opencontainers.image.authors = "binhex"
LABEL org.opencontainers.image.source = "https://github.com/binhex/arch-phantom"

# additional files
##################

# add supervisor conf file for app
ADD build/*.conf /etc/supervisor/conf.d/

# add bash script to run phantom
ADD run/nobody/*.sh /home/nobody/

# add install bash script
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

# expose port for phantom listen port
EXPOSE 19132

# expose port for phantom listen port
EXPOSE 19133

# set permissions
#################

# run script to set uid, gid and permissions
CMD ["/bin/bash", "/usr/local/bin/init.sh"]