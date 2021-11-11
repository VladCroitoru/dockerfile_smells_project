FROM ubuntu
MAINTAINER mwaeckerlin

ENV SRC '/data'
ENV DST '/video'
ENV FORMATS "ogv webm mp4"
ENV FLAGS_ogv "-c:v libtheora -c:a libvorbis -q:v 6 -q:a 5"
ENV FLAGS_webm "-vcodec libvpx -acodec libvorbis -f webm -aq 5 -ac 2 -qmax 25 -threads 2"
ENV FLAGS_mp4 "-vcodec libx264 -acodec aac -strict experimental -crf 19"
ENV LANG "en_US.UTF-8"

RUN apt-get update
RUN apt-get install -y libav-tools inotify-tools file language-pack-en
ADD start.sh /start.sh
CMD /start.sh

VOLUME /video