FROM phusion/baseimage:0.9.18
MAINTAINER thomfab

ENV DEBIAN_FRONTEND noninteractive

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

RUN apt-get update -qq && \
    apt-get install -qq --force-yes python wget && \
    apt-get autoremove && \
    apt-get autoclean

# download dropbox package
RUN mkdir -p /dropbox
RUN wget -O /dropbox/dropbox.tar.gz "http://www.dropbox.com/download/?plat=lnx.x86_64"
RUN cd /dropbox && tar -xvzf dropbox.tar.gz
RUN rm /dropbox/dropbox.tar.gz

# download dropbox command line
RUN wget -O /dropbox/dropbox.py "https://www.dropbox.com/download?dl=packages/dropbox.py"
RUN chmod +x /dropbox/dropbox.py
RUN chown -R nobody:users /dropbox
RUN chmod a+rwX /dropbox

EXPOSE 17500

VOLUME /dropbox/.dropbox
VOLUME /dropbox/Dropbox

# Add Dropbox to runit
RUN mkdir /etc/service/dropbox
ADD dropbox.sh /etc/service/dropbox/run
RUN chmod +x /etc/service/dropbox/run


# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
