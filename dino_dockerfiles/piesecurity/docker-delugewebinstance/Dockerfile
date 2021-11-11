FROM ubuntu
MAINTAINER Pie Secure <admin@pie-secure.org>
RUN echo "deb http://ppa.launchpad.net/deluge-team/ppa/ubuntu xenial main" >> /etc/apt/sources.list && \
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C5E6A5ED249AD24C && \
apt-get update && \
apt-get install -y deluged deluge-web deluge-console && \
adduser --system  --gecos "Deluge Service" --disabled-password --group --home /var/lib/deluge deluge
ADD deluged /etc/init.d/deluged
ADD deluge-daemon /etc/default/deluge-daemon
RUN chmod +x /etc/init.d/deluged
EXPOSE 8112
ENTRYPOINT chown deluge:deluge /var/lib/deluge && /etc/init.d/deluged start && su --shell /bin/bash -c deluge-console --login deluge && bash
#Running The Container Example
#Downloaded Files will be stored in what you define for /home/LocalFileStorage
#docker run -it -v /home/LocalFileStorage/:/var/lib/deluge -p 8112:8112 image_name
