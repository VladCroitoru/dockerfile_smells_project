FROM python:3.6-jessie

MAINTAINER mezz64 <jtmihalic@gmail.com>

ENV USER_ID=99
ENV GROUP_ID=100

#ENV EMBY_URL
#ENV EMBY_API_KEY
#ENV EMBY_USER_KEY
#ENV EMBY_UNC

RUN echo "deb http://deb.debian.org/debian jessie-backports main" >> /etc/apt/sources.list

# install packages
RUN apt-get update && \
    apt-get install -yq mkvtoolnix && \
    apt-get install -yq -t jessie-backports ffmpeg && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install requests

#make config folder
RUN \
 mkdir /config 

#Add start script
ADD start.sh /start.sh
RUN chmod +x /start.sh

#Add python script
ADD emby_eac3.py /emby_eac3.py
RUN chmod +x /emby_eac3.py

VOLUME ["/config"]

ENTRYPOINT ["/start.sh"]
