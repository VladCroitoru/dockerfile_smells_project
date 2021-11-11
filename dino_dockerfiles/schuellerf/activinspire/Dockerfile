FROM ubuntu:14.04
MAINTAINER Florian Schüller <florian.schueller@gmail.com>

COPY Promethean.asc /
COPY ia32-libs-dummy_1.0_all.deb /

ENV QT_X11_NO_MITSHM=1

# for flash
#  echo deb http://archive.ubuntu.com/ubuntu/ trusty multiverse >> /etc/apt/sources.list && \
# doesn't help anyway
RUN echo "deb http://activsoftware.co.uk/linux/repos/ubuntu precise oss non-oss" >> /etc/apt/sources.list && \
  apt-key add /Promethean.asc && \

  dpkg --add-architecture i386 && \
  apt-get update && \
  dpkg --install ia32-libs-dummy_1.0_all.deb && \
  apt-get -y install gstreamer0.10-plugins-good:i386 lib32z1 libasound2:i386 libXmu6:i386 libpulse-mainloop-glib0:i386 \
                     libicu52:i386 i3-wm i3status && \
  apt-get -y install activinspire:i386 && \
  ln -s /usr/lib/i386-linux-gnu/libicui18n.so.52 /usr/lib/i386-linux-gnu/libicui18n.so.42 && \
  rm -rf /var/lib/apt/lists/*

#dummy user
RUN adduser user

# Usually you want to start
# Xephyr :1 -ac -screen 800x600
# or similar
ENV DISPLAY=:1
ENV HOME=/home/user

RUN mkdir -p /home/user/.i3
RUN cp /etc/i3/config /home/user/.i3/config
RUN sed -i "s;^exec.*;exec /usr/local/bin/inspire;" /home/user/.i3/config

CMD [ "/usr/bin/i3" ]

