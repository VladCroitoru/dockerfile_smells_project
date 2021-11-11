FROM ingensi/play-framework 
MAINTAINER Timoteo Ponce <timo.slack@gmail.com>
# install ffmpeg
ADD ffmpeg.tar.gz /usr/lib/.
RUN ln -sf /usr/lib/ffmpeg/ffmpeg /usr/bin/ffmpeg && \
  ln -sf /usr/lib/ffmpeg/ffprobe /usr/bin/ffprobe && \
  chmod a+rx /usr/bin/ffmpeg && \
  chmod a+rx /usr/bin/ffprobe && \
  rm -rf /usr/lib/*.tar.gz 
