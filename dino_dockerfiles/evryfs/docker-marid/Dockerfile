FROM quay.io/evryfs/base-java:java8-20211026
ARG MARID_VERSION=2.15.0
RUN curl -L --silent https://s3-us-west-2.amazonaws.com/opsgeniedownloads/repo/opsgenie-marid_${MARID_VERSION}_all.deb -o /tmp/marid.dpkg && \
	dpkg -i /tmp/marid.dpkg && \
	rm /tmp/marid.dpkg && \
	mkdir -p /var/log/opsgenie/marid && \
	chown -R opsgenie:opsgenie /var/log/opsgenie
COPY run.sh /
COPY log4j.properties /etc/opsgenie/marid/log.properties
USER opsgenie
CMD ["/run.sh"]
