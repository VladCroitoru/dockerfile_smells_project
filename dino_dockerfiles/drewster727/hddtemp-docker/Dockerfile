#
# hddtemp Dockerfile
#

# Pull base image.
FROM ubuntu
MAINTAINER Drewster727

# Install hddtemp
RUN apt-get update && apt-get -y install build-essential hddtemp

COPY hddtemp.db /etc/

# Replace hddtemp with new build and cleanup
ADD files /temp
RUN rm -f /usr/sbin/hddtemp
RUN cp /temp/hddtemp /usr/sbin/
RUN chmod +x /usr/sbin/hddtemp
RUN rm -fdr /temp

# Define default command.
# example = -d --listen localhost --port 7634 /dev/s*
CMD hddtemp $HDDTEMP_ARGS
