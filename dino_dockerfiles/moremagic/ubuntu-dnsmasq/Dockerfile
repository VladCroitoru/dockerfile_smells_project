FROM ubuntu:15.04
MAINTAINER moremagic <itoumagic@gmail.com>

RUN apt-get update && apt-get install -y openssh-server openssh-client
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# tools install
RUN apt-get install -y vim curl wget
ADD dnsmasq/hostbyaddress /usr/local/sbin/hostbyaddress
RUN chmod +x /usr/local/sbin/hostbyaddress

# tinyproxy install
RUN apt-get install -y tinyproxy
RUN sed -i -e "s/^Allow /#Allow /" /etc/tinyproxy.conf
RUN sed -i -e "s/^User /#User /" /etc/tinyproxy.conf
RUN sed -i -e "s/^Group /#Group /" /etc/tinyproxy.conf

# dnsmasq install
RUN apt-get install -y dnsmasq
ADD dnsmasq/dnsmasq.conf /etc/dnsmasq.conf

RUN printf '#!/bin/bash \n\
cat /etc/resolv.conf > /etc/resolv.conf.base \n\
echo nameserver 127.0.0.1 > /etc/resolv.conf.append \n\
cat /etc/resolv.conf.append /etc/resolv.conf.base > /etc/resolv.conf \n\
 \n\
sed -i -e "s/^address=\/dev\/@@@@@/address=\/dev\/`hostbyaddress ${DISCOVERY}`/" /etc/dnsmasq.conf \n\
if [ -n "${DOMAIN+x}" ] ; then \n\
  sed -i -e "s/dev/${DOMAIN}/" /etc/dnsmasq.conf; \n\
fi \n\
/etc/init.d/dnsmasq start \n\
/etc/init.d/tinyproxy start \n\
/usr/sbin/sshd -D \n\
tail -f /dev/null \n\
' >> /etc/service.sh \
    && chmod +x /etc/service.sh

EXPOSE 22 8888 
CMD ["/etc/service.sh"]

