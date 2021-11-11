FROM debian:sid
MAINTAINER Adrien Lecharpentier <adrien.lecharpentier@gmail.com>

RUN apt-get update \
  && apt-get -y upgrade \
  && apt-get update \
  && apt-get install -y curl python2.7 ffmpeg
RUN ln -s $(which python2.7) /usr/local/bin/python
RUN curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
RUN chmod a+x /usr/local/bin/youtube-dl

VOLUME /downloads

COPY dl.sh /usr/local/bin/dl.sh
RUN chmod a+x /usr/local/bin/dl.sh
ENTRYPOINT ["/usr/local/bin/dl.sh"]
