FROM ubuntu:14.04


RUN apt-get update && apt-get install -y apcupsd python3 python3-pip
RUN pip3 install requests
RUN cp /etc/apcupsd/apcupsd.conf /opt/apcupsd.conf
COPY run.sh /opt/run.sh
RUN sed -i s/ISCONFIGURED=no/ISCONFIGURED=yes/g /etc/default/apcupsd
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN chmod +x /opt/run.sh

# APC name
ENV APC_NAME apc_name
# APC ip address (SNMP)
ENV APC_HOST localhost
# APC address post (SNMP default: 161)
ENV APC_PORT 161
# POST URL or URL path if CONSUL sets
ENV TARGET="http://localhost:9001/srv1"
# APC log status file
ENV STAT_FILE="/var/log/apcupsd.status"
# Check interval in seconds
ENV INTERVAL=3

ADD ./main.py /usr/src/app/


# Stat file
VOLUME /var/log

CMD ["/opt/run.sh"]