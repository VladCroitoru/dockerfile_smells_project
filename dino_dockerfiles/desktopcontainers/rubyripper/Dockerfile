FROM desktopcontainers/base-debian

MAINTAINER MarvAmBass (https://github.com/DesktopContainers)

RUN apt-get -q -y update \
 && apt-get -q -y install wget \
                          make \
                          cd-discid \
                          cdparanoia \
                          cdrdao \
                          flac \
                          lame \
                          wavpack \
                          normalize-audio \
                          ruby-gtk2 \
                          ruby-gettext \
                          ruby \
                          eject \
                          sox \
                          vorbisgain \
 && apt-get -q -y clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN wget -O /rubyripper.tar.gz https://github.com/bleskodev/rubyripper/archive/master.tar.gz \
 && tar xvf /rubyripper.tar.gz \
 && mv rubyripper-* /opt/rubyripper \
 && sed -i "s,deps.verify,#deps.verify',g" /opt/rubyripper/configure \
 && cd /opt/rubyripper \
 && ./configure --enable-lang-all --enable-gtk2 --enable-cli --prefix=/usr \
 && make install \
 && echo "rrip_gui \$*" >> /usr/local/bin/ssh-app.sh \
 \
 && mkdir -p /home/app/.config/rubyripper /rips \
 \
 && sed -i 's/starting services"/starting services"\n\nchmod a+rwx \/rips\n\n/g' /usr/local/bin/entrypoint.sh

COPY settings /home/app/.config/rubyripper/settings

RUN chown app.app -R /home/app/.config/rubyripper /rips \
 && usermod -aG cdrom app

VOLUME ["/rips"]
