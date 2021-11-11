FROM linuxserver/baseimage

# Install Depends
RUN apt-get update -q && \
apt-get install -qy python python-lxml wget unrar git python-cheetah python-pip python-dev libssl-dev && \
pip install pyopenssl==0.13.1 && \
apt-get clean && \
curl -o /tmp/rar.tar.gz http://www.rarlab.com/rar/rarlinux-x64-5.2.1b2.tar.gz&& \
tar xvf /tmp/rar.tar.gz  -C /tmp && \
cp -v /tmp/rar/*rar /usr/bin/ && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

#Mappings and Ports
EXPOSE 8081
VOLUME /config
VOLUME /downloads
VOLUME /series

#Adding Custom files
ADD init/ /etc/my_init.d/
ADD services/ /etc/service/
RUN chmod -v +x /etc/service/*/run
RUN chmod -v +x /etc/my_init.d/*.sh
