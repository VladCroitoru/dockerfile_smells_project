FROM vladshub/python-virtualenv
MAINTAINER Vladislav Shub <vlad6il@gmail.com>

EXPOSE 9000
ENV PYTHONIOENCODING "UTF-8"
COPY entrypoint.sh /
RUN virtualenv /env
ENV COUCHPOTATO_RUTRACKER_VERSION "master"
RUN git clone https://github.com/leugenea/cp-ru-server.git /couchpotatoserver-rutracker \
	&& cd /couchpotatoserver-rutracker \
	&& git checkout $COUCHPOTATO_RUTRACKER_VERSION

WORKDIR /couchpotatoserver-rutracker
RUN ["/env/bin/pip", "install", "-r", "requirements.txt"]
ENTRYPOINT ["/entrypoint.sh"]
