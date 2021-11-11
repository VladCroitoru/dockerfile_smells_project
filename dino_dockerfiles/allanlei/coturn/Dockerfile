# coturn 4.0.0.2
#
# VERSION               4.0.0.2
#
# Usage:
#
FROM 			debian:wheezy
MAINTAINER 		Allan Lei "allanlei@helveticode.com"


# Set the env variable DEBIAN_FRONTEND to noninteractive
ENV 			DEBIAN_FRONTEND noninteractive
ENV 			INITRD No


# Install updates
RUN 			apt-get update &&  apt-get -y upgrade


# Install coturn
ADD				coturn_4.0.0.2-1_amd64.deb /tmp/coturn_4.0.0.2-1_amd64.deb
RUN				apt-get install -y adduser krb5-locales libevent-core-2.0-5 libevent-extra-2.0-5 libevent-openssl-2.0-5 libevent-pthreads-2.0-5 libgcrypt11 libgnutls26 libgpg-error0 libgssapi-krb5-2 libhiredis0.10 libk5crypto3 libkeyutils1 libkrb5-3 libkrb5support0 libldap-2.4-2 libmysqlclient18 libp11-kit0 libpq5 libsasl2-2 libsasl2-modules libssl1.0.0 libtasn1-3 mysql-common telnet
RUN				dpkg -i /tmp/coturn_4.0.0.2-1_amd64.deb



# Cleanup
RUN 			apt-get -y autoremove && apt-get -y autoclean
RUN				rm -rf /tmp/coturn_4.0.0.2-1_amd64.deb


CMD				["turnserver"]