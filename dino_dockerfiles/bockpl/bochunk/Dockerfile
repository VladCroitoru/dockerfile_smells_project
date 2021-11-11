FROM ubuntu:20.04
MAINTAINER Seweryn Sitarski

# Instalacja klienta MFS
# Nieinteraktywne apt
#ENV DEBIAN_FRONTEND noninteractive
RUN apt update && apt install apt-utils && apt -y install wget && apt -y install gnupg && \
wget -O - https://ppa.moosefs.com/moosefs.key | apt-key add - && \
echo "deb http://ppa.moosefs.com/4.32.0/apt/ubuntu/focal focal main" > /etc/apt/sources.list.d/moosefs.list && \
apt update && \
apt -y install moosefs-pro-chunkserver xfsprogs 

#RUN apt-get -y install lvm2 && sed -i 's/use_lvmetad = 1/use_lvmetad = 0/' /etc/lvm/lvm.conf

# Czyszczenie apt-a
RUN apt -y purge wget && \
apt -y autoremove && \
apt -y clean

ADD start.sh /

EXPOSE 9422

CMD ["/bin/bash","-c","/start.sh"]
