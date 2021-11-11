FROM debian:latest

MAINTAINER Yury Evtikhov <yury@evtikhov.info>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -qy update && \
    apt-get -y  install makepasswd rcs perl-doc libio-tee-perl git libmail-imapclient-perl      \
                       libdigest-md5-file-perl libterm-readkey-perl libfile-copy-recursive-perl \
                       build-essential make automake libunicode-string-perl && \
    cpan -i Authen::NTLM Data::Uniqid Test::Pod && \
    git clone git://github.com/imapsync/imapsync.git /opt/imapsync && \
    cd /opt/imapsync && make install && make clean && \
    apt-get clean autoclean && \
    apt-get -y autoremove   && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/
	  

ENTRYPOINT ["/usr/bin/imapsync"]
