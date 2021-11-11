FROM jasonrivers/nagios:latest

RUN	sed -i 's/universe/universe multiverse/' /etc/apt/sources.list	;\
	apt-get update && apt-get install -y				\
                libwww-perl						\
                libterm-readkey-perl					\
                libjson-perl                                    &&      \
		apt-get clean
RUN     mkdir -p /opt/HS-Nagios-Plugins

ADD     nagios/spark.cfg /opt/nagios/etc/
ADD 	nagios/nagios.cfg /opt/nagios/etc/
RUN     cd /opt/HS-Nagios-Plugins                                &&      \
        git clone https://github.com/HariSekhon/nagios-plugins.git      &&      \
        cd /opt/HS-Nagios-Plugins/nagios-plugins			&&	\
        git clone https://github.com/HariSekhon/lib.git
