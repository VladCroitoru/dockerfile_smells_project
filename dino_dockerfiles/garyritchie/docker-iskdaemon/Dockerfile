# To use:
#	docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY --device /dev/dri jess/glxgears

FROM python:2.7-wheezy

# set wheezy apt-source
RUN echo "deb http://ftp.us.debian.org/debian/ wheezy main contrib non-free" > /etc/apt/sources.list.d/wheezy_main.list


RUN apt-get update && \
	apt-get install -y swig imagemagick libmagick++-dev python-dev

RUN git clone https://github.com/ricardocabral/iskdaemon.git

# Change the config for easier data management
RUN sed -i 's/databasePath = ~\/isk-db/databasePath = \/iskdaemon-db\/isk-db/g' /iskdaemon/src/isk-daemon.conf

WORKDIR /iskdaemon/src

RUN python setup.py install

CMD [ "python", "./iskdaemon.py" ]