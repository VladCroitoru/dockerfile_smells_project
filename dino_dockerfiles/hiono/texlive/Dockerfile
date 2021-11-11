FROM ubuntu:16.04
MAINTAINER onohr <bps@sculd.com>

ENV PKG="${PKG} wget tar unzip perl"
ENV PKG="${PKG} fontconfig fonts-takao-pgothic fonts-takao-gothic fonts-takao-mincho"
RUN apt-get -qq update && echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && ( apt-get -qq --force-yes -y --no-install-recommends install language-pack-ja ||  apt-get -qq --force-yes -y --no-install-recommends install language-pack-ja=1:14.04+20140410 ) && dpkg-reconfigure -f noninteractive locales && if [ "${PKG}" ];then apt-get -o Acquire::http::Dl-Limit=300 --force-yes -y --no-install-recommends upgrade && apt-get -o Acquire::http::Dl-Limit=300 --force-yes -y --no-install-recommends install ${PKG};fi && apt-get --force-yes -y --no-install-recommends install && apt-get autoremove && apt-get autoclean && apt-get clean && rm -rf "/var/cache/apt/archives/*" "/var/lib/apt/lists/*" && echo 'debconf debconf/frontend select Dialog' | debconf-set-selections
ENV TERM=xterm LANGUAGE=ja_JP:ja LANG=ja_JP.UTF-8 LC_TIME=POSIX
RUN /bin/cp -f /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN mkdir -p install-tl && wget -nv -O install-tl.tar.gz http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz && tar -xzf install-tl.tar.gz -C install-tl --strip-components=1
ADD texlive2016.profile install-tl/
RUN ( cd install-tl/ && ./install-tl --persistent-downloads --profile texlive2016.profile || ( ./install-tl --persistent-downloads --profile texlive2016.profile || ./install-tl --persistent-downloads --profile texlive2016.profile )) && rm install-tl.tar.gz && rm -r install-tl
RUN cp $(kpsewhich -var-value TEXMFSYSVAR)/fonts/conf/texlive-fontconfig.conf /etc/fonts/conf.d/09-texlive.conf
RUN fc-cache -fsv
CMD /bin/bash
