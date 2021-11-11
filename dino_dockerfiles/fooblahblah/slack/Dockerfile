#
# Props to Jessie Frazelle! https://blog.jessfraz.com/post/docker-containers-on-the-desktop/
#
# Run with something like:
#
# $ docker run -it --net host --cpuset-cpus 0 --memory 512mb -e DISPLAY=unix$DISPLAY -v ~/.config/Slack:/root/.config/Slack --device /dev/snd --name slack <imageid> slack
#
# To restart later you can use:
#
# $ docker restart slack
#

FROM ubuntu:15.10
MAINTAINER Jeff Simpson <jeff@syncrodoka.net>

ADD https://slack-ssb-updates.global.ssl.fastly.net/linux_releases/slack-desktop-2.0.1-amd64.deb /src/slack-desktop-2.0.1-amd64.deb

# Install Slack
RUN mkdir -p /usr/share/icons/hicolor && \
	apt-get update && apt-get install -y \
	ca-certificates \
	fonts-liberation \
        libasound2 \
        gconf2 \
        gconf-service \
        gvfs \
        hunspell \
        hunspell-en-us \
        libgtk2.0-0 \
        libnotify4 \
        libxtst6 \
        libxss1 \
        libnss3 \
        gvfs-bin \
        xdg-utils \
        apt-transport-https \
        python \
	wget \
	--no-install-recommends && \
	dpkg -i '/src/slack-desktop-2.0.1-amd64.deb' && \
	rm -rf /var/lib/apt/lists/* && \
	rm -rf /src/*.deb

COPY local.conf /etc/fonts/local.conf

ENTRYPOINT [ "/usr/bin/slack" ]
CMD [ "--user-data-dir=/data" ]
