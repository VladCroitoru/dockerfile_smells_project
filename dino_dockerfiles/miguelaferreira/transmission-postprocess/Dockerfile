FROM python:2.7
RUN apt-get update && apt-get -q -y install build-essential \
    && wget http://www.rarlab.com/rar/unrarsrc-5.4.4.tar.gz && tar xzf unrarsrc-5.4.4.tar.gz \
    && cd unrar && make -f makefile lib && make install-lib \
    && cd .. && rm -rf unrarsrc-5.4.4.tar.gz unrar && apt-get remove -y -q build-essential
VOLUME ['/downloads', '/processed']
ADD . /trdone
WORKDIR /trdone
RUN pip install -r requirements.txt

EXPOSE 80

ENV torrent_external=''
ENV torrent_internal=''
ENV puid='1000'
ENV pgid='1000'

ADD docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
