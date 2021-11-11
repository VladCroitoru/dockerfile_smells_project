FROM khirin/debian

ARG	UID="2000"
ARG	GID="2000"
ARG	PORT="4822"

ENV	PORT=${PORT}

LABEL 	maintainer="khirin" \
	name="Guacamole-server Image" \
        guacamole_version="0.9.12" \
	date="20170506" \
        image_version="1.0" \
	user="guacamole" \
	uid=${UID} \
	group="guacamole" \
	gid=${GID}

COPY ["sources/guacamole-server-0.9.12-incubating.tar.gz", "/tmp/"]

RUN	addgroup --gid ${GID} guacamole \
	&& adduser --gid ${GID} --disabled-password --gecos "Guacamole User" --shell /bin/bash -u ${UID} guacamole \
	&& cd /tmp \
	&& apt-get install -y 	libcairo2-dev \
				libjpeg62-turbo-dev \
				libpng12-dev \
				libossp-uuid-dev \
				libavcodec-dev \
				libavutil-dev \
				libswscale-dev \
				libfreerdp-dev \
				libpango1.0-dev \
				libssh2-1-dev \
				libtelnet-dev \
				libvncserver-dev \
				libpulse-dev \
				libssl-dev \
				libvorbis-dev \
				libwebp-dev \
	&& apt-get install -y gcc g++ make libtool \
	&& tar -xf guacamole-server-0.9.12-incubating.tar.gz \
	&& cd guacamole-server-*-incubating \
	&& ./configure \
	&& make \
	&& make install \
	&& ldconfig \
	&& cd /tmp \
	&& rm -rf /tmp/* \
	&& apt-get purge -y gcc g++ make libtool \
	&& apt-get clean

EXPOSE ${PORT}

USER guacamole

ENTRYPOINT /usr/local/sbin/guacd -f -b "0.0.0.0" -l ${PORT}
