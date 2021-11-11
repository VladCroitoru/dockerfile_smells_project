FROM phusion/baseimage:0.9.19

ARG DUPLICACY_VERSION=2.0.9
# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# ...put your own build instructions here...
RUN apt-get update -y && \ 
    apt-get dist-upgrade -y --no-install-recommends && \
    apt-get install -y --no-install-recommends \
       rsync rdiff-backup wget zip unzip vim git

       #build-essential libssl-dev libffi-dev
       #libxml2-dev libxslt1-dev zlib1g-dev
       #python-cherrypy3 python python-pysqlite2 libsqlite3-dev python-jinja2 python-setuptools python-babel
       #python-dev 
       #python-pip
#
RUN locale-gen en_US.UTF-8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install duplicacy 2.0.6
RUN cd /root && \
    wget --no-check-certificate -O duplicacy https://github.com/gilbertchen/duplicacy/releases/download/v$DUPLICACY_VERSION/duplicacy_linux_x64_$DUPLICACY_VERSION && \
    chmod a+x duplicacy && \
    cp duplicacy /usr/bin

# Activate SSH
RUN rm -f /etc/service/sshd/down

# Install startup scripts
RUN mkdir -p /etc/my_init.d
ADD cont-init.d/10-adduser                /etc/my_init.d/10-adduser
ADD cont-init.d/20-configure-ssh          /etc/my_init.d/20-configure-ssh
RUN chmod +x /etc/my_init.d/10-adduser    /etc/my_init.d/20-configure-ssh

EXPOSE 22

################### 
# Volumes expected to be mapped
# /config : config files (should be ro)
# expected to contain
# /config/ssh ( host and user key )
# /config/authorized_keys
# /config/tokens ( token files )
# /config/crontab
# /restore : where to restore files
# /datahome    : source directory for local backup (ro)
# /dataperso   : Source directory for local backup (ro)
# /pref-dirs   : Directory for  pref-dir option from Duplicacy
# /reports     : Directory for storing report files
# /restore     : Where restore commands should restore files
VOLUME /config /datahome /dataperso /pref-dirs /restore /reports



