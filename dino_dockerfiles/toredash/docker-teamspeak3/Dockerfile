FROM centos:7
MAINTAINER Tore S. Lønøy <tore.lonoy@gmail.com>
EXPOSE 9987/udp 30033 10011 41144

ENV ts3_version 3.0.13.8
ENV homedir /home/ts3

RUN \
useradd ts3 -U -m -s /bin/bash && \
yum install bzip2 /lib/ld-linux.so.2 -y && \
mkdir -p ${homedir}/data && \
mkdir -p ${homedir}/logs && \
ln -s ${homedir}/data/query_ip_blacklist.txt ${homedir}/query_ip_blacklist.txt && \
ln -s ${homedir}/data/query_ip_whitelist.txt ${homedir}/query_ip_whitelist.txt && \
ln -s ${homedir}/data/ts3server.sqlitedb ${homedir}/ts3server.sqlitedb && \
chown -R ts3:ts3 ${homedir}  && \
ln -s ${homedir} /ts3

USER ts3
WORKDIR ${homedir}
# Dedicated RUN for the binary
RUN curl -s http://teamspeak.gameserver.gamed.de/ts3/releases/${ts3_version}/teamspeak3-server_linux_x86-${ts3_version}.tar.bz2 | bunzip2 | tar -x --strip-components=1
CMD ["./ts3server_minimal_runscript.sh"]
