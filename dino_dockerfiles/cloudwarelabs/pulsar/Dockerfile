FROM cloudwarelabs/xorg:latest
MAINTAINER guodong <gd@tongjo.com>
RUN apt-get update
RUN apt-get install -y gnome-themes-standard xfwm4
RUN sed -i '2s/.*/gtk-theme-name = Adwaita/' /etc/gtk-3.0/settings.ini
RUN apt-get install -y libpulse0 libasound2
COPY pulsar-webrtc /usr/bin/pulsar-webrtc
COPY libprotobuf_lite.so /usr/lib/libprotobuf_lite.so
COPY libboringssl.so /usr/lib/libboringssl.so
COPY cloudware-run.sh /usr/bin/cloudware-run.sh
COPY cloudware-realrun.sh /usr/bin/cloudware-realrun.sh
CMD cloudware-run.sh
