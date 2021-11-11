FROM            debian:jessie
MAINTAINER      Zagorim

RUN \

        apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db && \
        echo "deb http://ftp.igh.cnrs.fr/pub/mariadb/repo/10.1/debian jessie main" > /etc/apt/sources.list.d/mariadb.list 
RUN apt-get update && \
        DEBIAN_FRONTEND=noninteractive apt-get install -yq  \
        python-software-properties \
        mariadb-server \
	supervisor \
        curl \
        git \
	php5-cli \
	php5-curl \
	php5-mysqlnd \
        procps \
	pwgen \
	wget \
	unzip && \
rm -rf /var/lib/apt/lists/* && apt-get autoclean
RUN wget http://files.v04.maniaplanet.com/server/ManiaplanetServer_2017-05-09.zip -O /opt/maniaplanet-server.zip && unzip \
/opt/maniaplanet-server.zip -d /opt/maniaplanet-server/ && rm /opt/maniaplanet-server.zip 

RUN     sed -i 's/^\(bind-address\s.*\)/# \1/' /etc/mysql/my.cnf && \
        echo "mysqld_safe &" > /tmp/config && \
        echo "mysqladmin --silent --wait=30 ping || exit 1" >> /tmp/config && \
        #echo "mysql -e 'GRANT ALL PRIVILEGES ON *.* TO \"root\"@\"%\" WITH GRANT OPTION;'" >> /tmp/config && \
        bash /tmp/config && \
        rm -f /tmp/config
RUN useradd -d /opt/maniaplanet-server/ -s /bin/bash shootmania
RUN mkdir -p /opt/maniaplanet-server/UserData/Packs/
RUN curl -L -o /opt/maniaplanet-server/UserData/Packs/SpeedBall.Title.Pack.Gbx https://v4.live.maniaplanet.com/ingame/public/titles/download/SpeedBall@steeffeen.Title.Pack.gbx
RUN cd /opt && git clone https://github.com/ManiaControl/ManiaControl.git && chown -R shootmania:games /opt/ManiaControl && chmod -R +x /opt/ManiaControl &&  chown -R shootmania:games /opt/maniaplanet-server
RUN echo "export TERM=xterm" >> /root/.bashrc
COPY dedicated_cfg.txt /opt/maniaplanet-server/UserData/Config/
COPY supervisord.conf /etc/supervisor/supervisord.conf
COPY firstrun.sh /opt/
COPY speedball.sh /opt/
COPY maniacontrol.sh /opt/
RUN usermod -a -G games shootmania
WORKDIR /opt/maniaplanet-server
CMD ["/usr/bin/supervisord"]

