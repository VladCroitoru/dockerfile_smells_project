FROM        buildpack-deps:jessie
MAINTAINER  Nala Ginrut
ENV         LANG C.UTF-8
ENV         GUILE_VERSION 2.1.8
RUN     echo "deb http://mirrors.ustc.edu.cn/debian jessie main contrib non-free" >> /etc/apt/sources.list \
	&& echo "deb-src http://mirrors.ustc.edu.cn/debian jessie main contrib non-free" >> /etc/apt/sources.list
RUN     apt-get update && apt-get upgrade -y && apt-get build-dep -y guile-2.0 && rm -rf /var/lib/apt/lists/*
RUN set -ex \
	&& wget -c http://ftp.gnu.org/gnu/lightning/lightning-2.1.0.tar.gz \
	&& tar xvzf lightning-2.1.0.tar.gz \
	&& rm -f lightning-2.1.0.tar.gz \
	&& cd lightning-2.1.0 \
	&& ./configure && make && make install && cd .. \
	\
	&& wget -c https://github.com/NalaGinrut/guile-tjit/archive/tjit-2.1.8.975-1f6fc-rebase.tar.gz \
	&& tar xvzf tjit-2.1.8.975-1f6fc-rebase.tar.gz \
	&& rm -f tjit-2.1.8.975-1f6fc-rebase.tar.gz \
	&& cd guile-tjit-tjit-2.1.8.975-1f6fc-rebase && ./autogen.sh && ./configure --enable-lightning && make \
	&& make install

CMD ["guile --tjit"]

