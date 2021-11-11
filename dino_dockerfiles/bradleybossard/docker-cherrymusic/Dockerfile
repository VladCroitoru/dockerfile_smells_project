FROM alpine:3.2
MAINTAINER Bradley Bossard <bradleybossard@gmail.com>

# install requirements
RUN apk update &&\
    apk add python3\
            ffmpeg\
            flac\
            curl

RUN pip3 install --upgrade pip &&\
    pip3 install cherrypy &&\
    pip3 install cherrymusic

ADD cherrymusic.conf /root/.config/cherrymusic/cherrymusic.conf

VOLUME ["/music", "/root/.local"]
EXPOSE 3000
CMD rm -f /root/.local/share/cherrymusic/cherrymusic.pid && exec cherrymusic --port 3000
