# Simple Firebird 2.0 DockerFile
FROM debian:jessie

MAINTAINER Ihsahn <ihsahn@users.noreply.github.com>

ENV DEBIAN_FRONTEND noninteractive


#get packages and install
RUN apt-get update && \
 apt-get install -qy curl && \
 curl -o libstdc++5_3.3.6-27.2_amd64.deb http://ftp.us.debian.org/debian/pool/main/g/gcc-3.3/libstdc++5_3.3.6-27.2_amd64.deb &&  \
 dpkg -i libstdc++5_3.3.6-27.2_amd64.deb && rm libstdc++5_3.3.6-27.2_amd64.deb && \
 curl -O -L http://downloads.sourceforge.net/project/firebird/firebird-linux-amd64/2.5.5-Release/FirebirdSS-2.5.5.26952-0.amd64.tar.gz && tar -xvf FirebirdSS-2.5.5.26952-0.amd64.tar.gz && \
 grep -v "InteractiveInstall=1" FirebirdSS-2.5.5.26952-0.amd64/install.sh | grep -v "Press Enter to start installation" > FirebirdSS-2.5.5.26952-0.amd64/fbinst.sh

#cleanup
RUN cd ./FirebirdSS-2.5.5.26952-0.amd64 && sh ./fbinst.sh && cd / && rm -rf FirebirdSS-2.5.5.26952-0.amd64*

#entry point
COPY firebird-docker-entrypoint.sh /
RUN chmod +x /firebird-docker-entrypoint.sh

VOLUME ["/var/lib/firebird/data"]

ENTRYPOINT ["/firebird-docker-entrypoint.sh"]

EXPOSE 3050/tcp

CMD ["firebird"]
