from debian

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get install -y git curl apache2 binutils

WORKDIR /root

RUN git clone https://github.com/tpaskett/meshchat.git

WORKDIR /root/meshchat

RUN ./build
RUN dpkg -i meshchat_*_all.deb

EXPOSE 80

ENV MESH_ZONE=MeshChat
ENV LOCAL_NODE=localnode

VOLUME ["/var/www/html/meshchat/db/"]

CMD sed -i 's|.*$pi_zone.*|our $pi_zone = '"\"$MESH_ZONE\";|" /usr/lib/cgi-bin/meshchatconfig.pm  && \
 sed -i 's|.*$local_meshchat_node.*|our $local_meshchat_node = '"\"$LOCAL_NODE\";|" /usr/lib/cgi-bin/meshchatconfig.pm && \
 echo nameserver $LOCAL_NODE > /etc/resolv.conf && apache2ctl start && meshchatsync
