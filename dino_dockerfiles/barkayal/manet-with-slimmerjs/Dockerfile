FROM node:6.10

EXPOSE 8891

COPY ./debian-contrib.list /etc/apt/sources.list.d/debian-contrib.list
COPY ./debian-mozilla.list /etc/apt/sources.list.d/debian-mozilla.list

RUN wget -O /tmp/pkg-mozilla-archive-keyring_1.1_all.deb mozilla.debian.net/pkg-mozilla-archive-keyring_1.1_all.deb && \
    dpkg -i /tmp/pkg-mozilla-archive-keyring_1.1_all.deb && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get -y install build-essential libfontconfig1 xvfb && \
    apt-get -y install xfonts-100dpi xfonts-100dpi-transcoded xfonts-75dpi xfonts-75dpi-transcoded xfonts-scalable && \
    apt-get -y install cabextract ttf-mscorefonts-installer && \
    apt-get -y install -t jessie-backports firefox && \
    npm install -g phantomjs-prebuilt slimerjs manet && \
    sed -ie 's/letter/A4/g' /usr/local/lib/node_modules/manet/src/scripts/screenshot.js && \
    sed -ie 's/MaxVersion=.*/MaxVersion=*/g' /usr/local/lib/node_modules/slimerjs/src/application.ini && \
    curl -Lo /usr/local/sbin/init https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 && \
    chmod a+x /usr/local/sbin/init

ENTRYPOINT ["/usr/local/sbin/init", "/usr/local/bin/manet", "--command=timeout -s9 30 xvfb-run -a slimerjs", "--cache=0", "--cleanupStartup=true", "--cleanupRuntime=true", "--cors=true", "--force=true"]
