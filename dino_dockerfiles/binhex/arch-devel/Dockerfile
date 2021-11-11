FROM binhex/arch-base:latest
LABEL org.opencontainers.image.authors = "binhex"
LABEL org.opencontainers.image.source = "https://github.com/binhex/arch-devel"

# additional files
##################

# add install bash script
ADD build/root/*.sh /root/

# get release tag name from build arg
ARG release_tag_name

# install app
#############

# run bash script to update base image, set locale, install supervisor and cleanup
RUN chmod +x /root/*.sh && \
	/bin/bash /root/install.sh "${release_tag_name}"

# run bash
CMD ["/bin/bash"]
