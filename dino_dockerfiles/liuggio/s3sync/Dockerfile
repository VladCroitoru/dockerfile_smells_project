# Use phusion/baseimage
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md

FROM phusion/baseimage:latest
MAINTAINER Giulio De Donato <liuggio@gmail.com>

RUN apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get -qq install s3cmd python-pip && \
  pip install python-magic

RUN mkdir                     /etc/service/s3sync
ADD build/s3sync.sh           /etc/service/s3sync/run
RUN chmod +x                  /etc/service/s3sync/run
ADD build/.s3cfg.template     /etc/.s3cfg.template

CMD ["/sbin/my_init"]

# Clean up APT when done.
RUN DEBIAN_FRONTEND="noninteractive" apt-get purge -y python-pip && apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*