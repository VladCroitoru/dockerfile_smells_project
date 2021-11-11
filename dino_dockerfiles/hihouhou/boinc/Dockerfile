#
# Boinc Dockerfile
#
# https://github.com/
#

# Pull base image.
FROM debian:latest

MAINTAINER hihouhou < hihouhou@hihouhou.com >


# Update & install packages for boinc
RUN apt-get update && \
    apt-get install -y boinc-client 

#Configure boinc 
RUN mkdir -p /boinc/slots
ADD cc_config.xml /boinc/
#ADD remote_hosts.cfg /boinc/


EXPOSE 31416

CMD ["boinc", "--dir", "/boinc"]
