FROM phusion/baseimage:0.9.19
MAINTAINER garth@garthk.com
# https://github.com/phusion/baseimage-docker#enabling-ssh
RUN rm -f /etc/service/sshd/down
ADD sources.list /etc/apt/
RUN apt-get update \
 && apt-get upgrade -y -o Dpkg::Options::="--force-confold" \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y mercurial mercurial-server \
 && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN  mv /var/lib/mercurial-server /data \
 && ln -sf /data /var/lib/mercurial-server
ADD refresh-auth /etc/my_init.d/
VOLUME ["/data"]
WORKDIR /data
EXPOSE 22
CMD ["/sbin/my_init"]
ONBUILD ADD authorized_keys /etc/mercurial-server/keys/root/init
ONBUILD ADD authorized_keys /root/.ssh/
ONBUILD RUN chmod 0600 /root/.ssh/authorized_keys
