FROM besn0847/desktop-light:1.0
MAINTAINER Franck Besnard <franck@besnard.mobi>

ENV DEBIAN_FRONTEND noninteractive
ENV HOME /root

RUN apt-get update \
        && apt-get install -y --force-yes --no-install-recommends \
                curl git bluefish firefox software-properties-common lame libwebkitgtk-1.0-0 \
	&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections \
	&& add-apt-repository -y ppa:webupd8team/java \
	&& apt-get update \
	&& apt-get install -y oracle-java8-installer \
        && apt-get autoclean \
        && apt-get autoremove \
        && rm -rf /var/lib/apt/lists/*

RUN cd /root \
    && curl -O -L http://www.xmind.net/xmind/downloads/xmind-linux-3.5.3.201506180105_amd64.deb \
    && dpkg -i /root/xmind-linux-3.5.3.201506180105_amd64.deb \
    && rm -f /root/xmind-linux-3.5.3.201506180105_amd64.deb \
    && ln -s /usr/bin/XMind /usr/bin/Xmind

RUN cd /root \ 
	&& curl -O -L http://dist.springsource.com/release/STS/3.7.0.RELEASE/dist/e4.5/spring-tool-suite-3.7.0.RELEASE-e4.5-linux-gtk-x86_64.tar.gz \
	&& tar xvfz spring-tool-suite-3.7.0.RELEASE-e4.5-linux-gtk-x86_64.tar.gz \
	&& mkdir -p /home/default \
	&& mv sts-bundle/sts-3.7.0.RELEASE /home/default \
	&& chmod -R og+rw /home/default/sts-3.7.0.RELEASE \
	&& rm -f /root/spring-tool-suite-3.7.0.RELEASE-e4.5-linux-gtk-x86_64.tar.gz \
	&& rm -rf /root/sts-bundle

ADD springsource-toolsuite.desktop /usr/share/applications/
ADD startup.sh /

RUN chmod +x /startup.sh

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

EXPOSE 5900
WORKDIR /root
ENTRYPOINT ["/startup.sh"]
