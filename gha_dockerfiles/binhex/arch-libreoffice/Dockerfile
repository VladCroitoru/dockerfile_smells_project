FROM binhex/arch-int-gui:latest
LABEL org.opencontainers.image.authors = "binhex"
LABEL org.opencontainers.image.source = "https://github.com/binhex/arch-libreoffice"

# additional files
##################

# add install and packer bash script
ADD build/root/*.sh /root/

# get release tag name from build arg
ARG release_tag_name

# add pre-configured config files for libreoffice
ADD config/nobody/ /home/nobody/

# add expect script for build of libreoffice
ADD config/root/ /root/

# install app
#############

# make executable and run bash scripts to install app
RUN chmod +x /root/*.sh && \
	/bin/bash /root/install.sh "${release_tag_name}"

# docker settings
#################

# set permissions
#################

# run script to set uid, gid and permissions
CMD ["/bin/bash", "/usr/local/bin/init.sh"]
