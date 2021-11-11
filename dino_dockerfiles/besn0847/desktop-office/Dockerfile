FROM besn0847/desktop-light:1.0
MAINTAINER Franck Besnard <franck@besnard.mobi>

ENV DEBIAN_FRONTEND noninteractive
ENV HOME /root

RUN apt-get update \
        && apt-get install -y --force-yes --no-install-recommends \
                curl libreoffice default-jre lame libwebkitgtk-1.0-0 \
        && apt-get autoclean \
        && apt-get autoremove \
        && rm -rf /var/lib/apt/lists/*

RUN cd /root \
	&& curl -O -L http://www.xmind.net/xmind/downloads/xmind-linux-3.5.3.201506180105_amd64.deb \
	&& dpkg -i /root/xmind-linux-3.5.3.201506180105_amd64.deb \
	&& rm -f /root/xmind-linux-3.5.3.201506180105_amd64.deb \
	&& ln -s /usr/bin/XMind /usr/bin/Xmind

EXPOSE 5900
WORKDIR /root
ENTRYPOINT ["/startup.sh"]
