FROM desktopcontainers/base-debian

MAINTAINER MarvAmBass (https://github.com/DesktopContainers)

RUN apt-get -q -y update \
 && apt-get -q -y install wget \
                          handbrake \
                          vlc \
 && apt-get -q -y clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
 \
 && wget "http://download.videolan.org/debian/stable/libdvdcss2_1.2.13-0_amd64.deb" \
 && dpkg -i libdvdcss2_*.deb \
 && echo "handbrake \$*" >> /usr/local/bin/ssh-app.sh \
 && mkdir -p /rips /home/app/Desktop/ \
 && chown app.app -R /home/app/ /rips \
 && usermod -aG cdrom app \
 \
 && sed -i 's/starting services"/starting services"\n\nchmod a+rwx \/rips\n\n/g' /usr/local/bin/entrypoint.sh
    
COPY presets /home/app/Desktop/HandbrakePresets

RUN chown app.app -R /home/app/

VOLUME ["/rips"]
