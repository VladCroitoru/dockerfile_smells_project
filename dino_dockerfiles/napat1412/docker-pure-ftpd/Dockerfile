
FROM debian:jessie

# feel free to change this ;)
MAINTAINER Andrew Stilliard <andrew.stilliard@gmail.com>

# properly setup debian sources
ENV DEBIAN_FRONTEND noninteractive
RUN echo "deb http://http.debian.net/debian jessie main\n\
deb-src http://http.debian.net/debian jessie main\n\
deb http://http.debian.net/debian jessie-updates main\n\
deb-src http://http.debian.net/debian jessie-updates main\n\
deb http://security.debian.org jessie/updates main\n\
deb-src http://security.debian.org jessie/updates main\n\
" > /etc/apt/sources.list
RUN apt-get -y update

# install package building helpers
RUN apt-get -y --force-yes --fix-missing install dpkg-dev debhelper

# install dependancies
RUN apt-get -y build-dep pure-ftpd

# build from source
RUN mkdir /tmp/pure-ftpd/ && \
	cd /tmp/pure-ftpd/ && \
	apt-get source pure-ftpd && \
	cd pure-ftpd-* && \
	./configure --with-tls && \
	sed -i '/^optflags=/ s/$/ --without-capabilities/g' ./debian/rules && \
	dpkg-buildpackage -b -uc

# install the new deb files
RUN dpkg -i /tmp/pure-ftpd/pure-ftpd-common*.deb
RUN apt-get -y install openbsd-inetd
RUN dpkg -i /tmp/pure-ftpd/pure-ftpd_*.deb

# Prevent pure-ftpd upgrading
RUN apt-mark hold pure-ftpd pure-ftpd-common

# setup ftpgroup and ftpuser
RUN groupadd ftpgroup
RUN useradd -g ftpgroup -d /home/ftpusers -s /dev/null ftpuser

# rsyslog for logging (ref https://github.com/stilliard/docker-pure-ftpd/issues/17)
RUN apt-get install -y rsyslog && \
	echo "" >> /etc/rsyslog.conf && \
	echo "#PureFTP Custom Logging" >> /etc/rsyslog.conf && \
	echo "ftp.* /var/log/pure-ftpd/pureftpd.log" >> /etc/rsyslog.conf && \
	echo "Updated /etc/rsyslog.conf with /var/log/pure-ftpd/pureftpd.log"

# setup run/init file
COPY run.sh /run.sh
RUN chmod u+x /run.sh

# default publichost, you'll need to set this for passive support
ENV MAX_CLIENT_NUMBER 50
ENV MAX_CLIENTperIP 10
ENV SERVICE_PORT 21
ENV PASSIVE_PORTRANGE 30000:30009
ENV OPENSSL_SUBJ "/C=TH"

# couple available volumes you may want to use
VOLUME ["/home/ftpusers", "/etc/pure-ftpd/passwd"]


# Secure defaults, ref: https://github.com/stilliard/docker-pure-ftpd/issues/10
RUN cd /etc/pure-ftpd/conf/ && \
	echo "yes" | tee AntiWarez ChrootEveryone CreateHomeDir CustomerProof Daemonize DontResolve IPV4Only NoAnonymous NoChmod NoRename ProhibitDotFilesRead ProhibitDotFilesWrite LogPID NATmode && \
	echo "no" | tee AllowAnonymousFXP AllowDotFiles AllowUserFXP AnonymousCanCreateDirs AnonymousCantUpload AnonymousOnly AutoRename BrokenClientsCompatibility CallUploadScript DisplayDotFiles IPV6Only KeepAllFiles PAMAuthentication UnixAuthentication VerboseLog

# startup
CMD /run.sh --bind $SERVICE_PORT -p $PASSIVE_PORTRANGE -c $MAX_CLIENT_NUMBER -C $MAX_CLIENTperIP -l puredb:/etc/pure-ftpd/pureftpd.pdb -E -j -R

