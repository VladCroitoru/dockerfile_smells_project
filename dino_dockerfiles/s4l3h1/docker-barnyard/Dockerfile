FROM s4l3h1/docker-snort:latest
MAINTAINER Muhammad Salehi <salehi1994@gmail.com>
ENV DEBIAN_FRONTEND noninteractive
ENV COVERALLS_TOKEN [secure]
ENV CC gcc
ENV CXX g++
WORKDIR /opt/snort_src
RUN apt-get update && apt upgrade -y ;\
apt-get install cron net-tools ethtool inetutils-ping git wget build-essential libpcap-dev libpcre3-dev libdumbnet-dev bison flex zlib1g-dev liblzma-dev openssl libssl-dev libnghttp2-dev  python-pip supervisor libmysqlclient-dev mysql-client autoconf libtool libcrypt-ssleay-perl liblwp-useragent-determined-perl -y ;\
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* ;\
wget https://github.com/firnsy/barnyard2/archive/master.tar.gz -O barnyard2-Master.tar.gz ;\
tar zxvf barnyard2-Master.tar.gz ;\
cd barnyard2-master ; autoreconf -fvi -I ./m4 ; cd .. ;\
ln -s /usr/include/dumbnet.h /usr/include/dnet.h ;\
ldconfig ;\
cd barnyard2-master; ./configure --with-mysql --with-mysql-libraries=/usr/lib/x86_64-linux-gnu; make; make install; cd .. ;\
/usr/local/bin/barnyard2 -V ;\
cp -fv /opt/snort_src/barnyard2-master/etc/barnyard2.conf /etc/snort/ ;\
mkdir /var/log/barnyard2 ;\
chown snort.snort /var/log/barnyard2 ;\
touch /var/log/snort/barnyard2.waldo ;\
chown snort.snort /var/log/snort/barnyard2.waldo ;\
chmod o-r /etc/snort/barnyard2.conf
ADD superv.conf /etc/supervisor/conf.d/
ADD barnyard.sh /opt/
RUN chmod +x /opt/barnyard.sh
ENTRYPOINT ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]
