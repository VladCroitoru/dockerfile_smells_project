FROM python:2.7.18-buster
#=====================#
# Setup Prerequisites #
#=====================#
RUN apt-get update && apt-get install -y \
	apache2 \
	git \
	vim \
	&& a2enmod cgi \
	&& service apache2 restart \
	&& rm -rf /var/lib/apt/lists/*
#===============================#
# Docker Image Configuration	#
#===============================#
LABEL org.opencontainers.image.source='https://github.com/eipm/beacon' \
	Description='Beacon' \
	Vendor='Englander Institute for Precision Medicine' \
	maintainer='als2076@med.cornell.edu' \
	base_image='python' \
	base_image_version='2.7.18-buster'
#=====================#
# Install Beacon 	  #
#=====================#
ENV BEACON_DIR /var/www/html/beacon
WORKDIR ${BEACON_DIR}
RUN git clone https://github.com/maximilianh/ucscBeacon.git \
	&& cd ucscBeacon/ \
	&& sed -i "s/'server.socket_port': port/'server.socket_port': port, 'server.socket_host': '0.0.0.0'/g" query
#=====================#
# Configure Beacon 	  #
#=====================#
RUN echo "ServerName localhost" | tee /etc/apache2/conf-available/fqdn.conf \
	&& a2enconf fqdn
COPY config/beacon.conf ${BEACON_DIR}/beacon.conf
COPY config/apache2.conf /etc/apache2/apache2.conf
COPY app ${BEACON_DIR}
#=====================#
# Beacon Startup 	  #
#=====================#
CMD /usr/sbin/apache2ctl -D FOREGROUND
