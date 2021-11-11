FROM lsiobase/alpine.python 
MAINTAINER  ajw107 (Alex Wood)

ENV PORT 32500
ENV WEBROOT ""
ENV PUID 999
ENV PGID 999
ENV CONFIG "/config"
ENV APP "/app"
ENV APPNAME "comicstreamer"
ENV DATA "/comics"

#make life easy for yourself
ENV TERM=xterm-color
#this only works on alpine images for some reason
#and I've just changed to an alpine image, ah well.....
#RUN echo $'#!/bin/bash\nls -alF --color=auto --group-directories-first --time-style=+"%H:%M %d/%m/%Y" --block-size="\'1" $@' > /usr/bin/ll
COPY root/ /
RUN chmod +x /usr/bin/ll

RUN \
   apk update && \
   apk add --no-cache \
#        p7zip \
#        unrar \
#        unzip \
#	 python \
	nano \
	git \
	wget \
	avahi-compat-libdns_sd &&\
 
# install build packages
   apk add --no-cache --virtual=build-dependencies \
       g++ \
       gcc \
#	py-pip \
       python-dev \
       libjpeg-turbo-dev \
       zlib-dev 

#make the message bus dir for avahi bonjour announcing thing
RUN mkdir -p /var/run/dbus

# Pybonjour must be installed manually
RUN pip install --no-cache-dir -U \
  https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/pybonjour/pybonjour-1.1.1.tar.gz

#install the rest of the dependencies
RUN pip install --no-cache-dir -U \
                 argh \
		 backports.ssl-match-hostname \
		 certifi \
		 configobj \
		 natsort \
		 pathtools \
		 Pillow \
		 PyPDF2 \
		 python-dateutil \
		 PyYAML \
		 six \
		 SQLAlchemy \
		 tornado \
		 unrar \
		 watchdog \
		 paver \
		 pylzma

#create the specified group
#RUN addgroup abc --gid "${PGID}"

# Run commands as the comicstreamer user
#RUN adduser \ 
#	--disabled-login \ 
#	--shell /bin/bash \ 
#	--gecos "" \
#        --uid "${PUID}" \
#	--gid "${PGID}" \
#        abc

# Copy & rights to folders
COPY run.sh /home/abc/run.sh

RUN chmod 777 /home/abc/run.sh

# create the comics directory
#RUN mkdir "${DATA}" && chown "${PUID}:${PGID}" "${DATA}"

# create app and config directories

#RUN mkdir -p "${APP}" && chown "${PUID}:${PGID}" "${APP}"

#RUN mkdir -p "${CONFIG}" && chown "${PUID}:${PGID}" "${CONFIG}"

#WORKDIR "${APP}"

#grab the latest version from git
#RUN git clone https://github.com/Tristan79/ComicStreamer.git "${APPNAME}"

#WORKDIR "${APP}/${APPNAME}"

#make sure chosen user can run it
#RUN chown -R "${PUID}:${PGID}" "${APP}/${APPNAME}"

#USER abc 

#RUN paver libunrar

# cleanup
RUN apk del --purge \
	build-dependencies && \
    rm -rf \
        /root/.cache \
	/tmp/* \
	/var/lib/apt/lists/* \
        /var/tmp/*

# Expose default port : 32500
EXPOSE ${PORT}
# Expose User and group id 
EXPOSE ${PUID}
EXPOSE ${PGID}

VOLUME ${APP}
VOLUME ${CONFIG}
VOLUME ${DATA}
VOLUME /var/run/dbus

ENTRYPOINT ["/home/abc/run.sh"]
