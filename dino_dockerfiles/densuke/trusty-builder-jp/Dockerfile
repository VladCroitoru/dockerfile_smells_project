FROM densuke/ubuntu-jp-remix:trusty
MAINTAINER densuke

RUN apt-get update
RUN apt-get install -y ubuntu-defaults-builder wget devscripts
RUN apt-get clean
RUN mkdir /target 
RUN mkdir /builder
ENV HOME /root
WORKDIR /builder
RUN wget -nv http://archive.ubuntulinux.jp/ubuntu/pool/main/u/ubuntu-defaults-ja/ubuntu-defaults-ja_14.04-0ubuntu1~ja6.dsc http://archive.ubuntulinux.jp/ubuntu/pool/main/u/ubuntu-defaults-ja/ubuntu-defaults-ja_14.04-0ubuntu1~ja6.tar.gz
RUN dpkg-source -x ubuntu-defaults-ja_14.04-0ubuntu1~ja6.dsc && rm *.tar.gz *.dsc && mv -v * config
ADD build.sh /builder/
RUN chmod +x /builder/build.sh
ENTRYPOINT ["/builder/build.sh"]
