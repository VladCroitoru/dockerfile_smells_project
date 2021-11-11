FROM golang:1.4.2

# Install webkit/gtk for webloop(prerender for golang)
RUN apt-get update && apt-get install -y \
    libwebkit2gtk-3.0-dev \
    xvfb \
    && rm -rf /var/lib/apt/lists/*


ENV DISPLAY :99

ADD xvfb-init /etc/init.d/xvfb
RUN chmod a+x /etc/init.d/xvfb

ADD ./init.sh /init.sh
RUN chmod a+x /init.sh

ENTRYPOINT /init.sh
