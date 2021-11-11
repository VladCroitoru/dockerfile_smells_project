FROM jasonrivers/nagios:4.4.6

LABEL maintainer=coen.vanleeuwen@tno.nl

ENV CEPH_PLUGIN /opt/ceph-nagios-plugin

RUN apt-get update && apt-get install -y ceph freeipmi-tools && \
	apt-get clean && rm -Rf /var/lib/apt/lists/*

RUN git clone https://github.com/ceph/ceph-nagios-plugins.git && \
	mkdir -p ${CEPH_PLUGIN}/lib && \
	mkdir -p ${CEPH_PLUGIN}/cfg && \
	cp ceph-nagios-plugins/src/* ${CEPH_PLUGIN}/lib && \
	sed "s,/usr/lib/nagios/plugins,${CEPH_PLUGIN}/lib," ceph-nagios-plugins/config/ceph.cfg > ${CEPH_PLUGIN}/cfg/ceph.cfg

ADD start.sh /usr/local/bin/start_nagios_ceph

RUN chmod +x /usr/local/bin/start_nagios_ceph
