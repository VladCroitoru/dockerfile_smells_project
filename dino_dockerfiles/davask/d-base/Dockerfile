FROM davask/d-debian:9.x

MAINTAINER davask <admin@davask.com>
USER root
# Update packages
RUN apt update && \
apt install -y \
acl \
apt-utils \
binutils \
build-essential \
cron \
curl \
expect \
git \
perl \
htop \
unzip
RUN apt-get upgrade -y && \
apt-get autoremove -y && \
apt-get clean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY ./build/dwl/init.sh \
/dwl/
RUN chmod +x /dwl/init.sh && chown root:sudo -R /dwl
USER admin
