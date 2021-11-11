FROM debian:8.9 
MAINTAINER admin <evgeniy@kolesnyk.ru> 

RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install build-essential autoconf libtool gcc g++ make git-core wget p7zip-full libncurses5-dev zlib1g-dev libbz2-dev openssl libssl-dev libreadline6-dev libboost-dev libboost-thread-dev libboost-system-dev libboost-filesystem-dev libboost-program-options-dev libboost-iostreams-dev screen libzmq-dev libmysqlclient-dev libmysql++-dev screen curl apache2 php5 php5-mysql -y

RUN curl -o /root/cmake-3.9.4.tar.gz https://cmake.org/files/v3.9/cmake-3.9.4.tar.gz
RUN cd /root && tar xzf cmake-3.9.4.tar.gz
RUN cd /root/cmake-3.9.4 && ./configure && make && make install
RUN rm -rf /root/cmake-3.9.4 && rm -f /root/cmake-3.9.4.tar.gz

RUN useradd -ms /bin/bash server
RUN mkdir -p /home/server/wow && mkdir -p /home/server/source
RUN cd /home/server/source && git clone git://github.com/TrinityCore/TrinityCore.git  && mkdir -p /home/server/source/TrinityCore/build
RUN cd /home/server/source/TrinityCore && git checkout -b 3.3.5 origin/3.3.5
RUN cd /home/server/source/TrinityCore/build && cmake ../ -DCMAKE_INSTALL_PREFIX=/home/server/wow

COPY setup-mysql.sh /root/setup-mysql.sh
RUN chmod +x /root/setup-mysql.sh
RUN /root/setup-mysql.sh
RUN rm -f /root/setup-mysql.sh

RUN curl -o /home/server/wow.tar.gz http://dark-games.org.ua/files/wow3.3.5a/wow.tar.gz
RUN tar -xvzf /home/server/wow.tar.gz -C /home/server && rm -f /home/server/wow.tar.gz
RUN mv /home/server/wow/etc/authserver.conf.dist /home/server/wow/etc/authserver.conf
RUN mv /home/server/wow/etc/worldserver.conf.dist /home/server/wow/etc/worldserver.conf
RUN curl -o /home/server/wow/bin/maps.tar http://dark-games.org.ua/files/wow3.3.5a/maps.tar
RUN cd /home/server/wow/bin && tar -xvf maps.tar && rm -f maps.tar

RUN curl -o /var/www/html/reg.tar http://dark-games.org.ua/files/wow3.3.5a/reg.tar
RUN cd /var/www/html &&  echo "<head><meta http-equiv='refresh' content='0; url=/index.php' /></head>" > /var/www/html/index.html && tar -xvf reg.tar && rm -f /var/www/html/reg.tar

COPY restart_authserver.sh /home/server/wow/restart_authserver.sh
COPY restart_worldserver.sh /home/server/wow/restart_worldserver.sh
COPY update.sh /root/update.sh
COPY restart_all.sh /root/restart_all.sh
RUN chmod +x /home/server/wow/restart_authserver.sh
RUN chmod +x /home/server/wow/restart_worldserver.sh
RUN chmod +x /root/update.sh
RUN chmod +x /root/restart_all.sh

EXPOSE 22 3306 3724 8085
ENTRYPOINT /root/restart_all.sh
