FROM java:7

RUN apt-get update ; \
  apt-get -y install xvfb \
    vnc4server \
    tightvncserver \
    libswt-gnome-gtk-3-jni \
    ratpoison ; \
  apt-get clean

RUN useradd -u 1999 -U -m -d /vnc vnc

COPY entrypoint.sh /vnc/entrypoint.sh

USER vnc

CMD [ "/usr/bin/tightvncserver", "--help" ]

ENTRYPOINT [ "/bin/bash", "/vnc/entrypoint.sh" ]
