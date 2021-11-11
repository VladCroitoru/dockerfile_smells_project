FROM debian:sid
MAINTAINER Andrea Capriotti <capriott@gmail.com>

VOLUME /home

RUN sed -i '0,/RE/s/main/main contrib/' /etc/apt/sources.list

RUN apt-get update && apt-get upgrade -yq && apt-get install -yq --install-recommends \
    wget firefox libgl1-mesa-dri libvdpau-va-gl1 va-driver-all fonts-dejavu \
    gstreamer1.0-plugins-good gstreamer1.0-x gstreamer1.0-plugins-good libcanberra-gtk3-module \
    gstreamer1.0-plugins-base gstreamer1.0-alsa xdg-utils libxss1 pulseaudio && \
    apt-get clean && rm -rf /var/lib/apt/lists/ && \
    echo enable-shm=no >> /etc/pulse/client.conf

RUN echo '\n// Disable tabs autostart as a workaround for random crashing\n\
// See https://github.com/SeleniumHQ/docker-selenium/issues/388\n\
lockPref("browser.tabs.remote.autostart.2", false);' >> /etc/firefox/firefox.js

ENV PULSE_SERVER /run/pulse/native

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

#CMD ["/usr/bin/firefox" ,"-new-instance"]
CMD ["firefox"]
