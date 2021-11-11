# barcode_mail_keeper
#
# @version 	0.3
# @author 	asda <asda@asda.ru>
FROM ubuntu:16.04

MAINTAINER Andrey Mamaev


RUN apt-get update && \
	apt-get install -y \
		pkg-config \
		gcc \
		g++ \
		libncurses5-dev \ 
		libtool \
		make \
		libxml2-dev \
		libperl-dev \
		libtiff-dev \
		libfreetype6-dev \
		libbz2-dev \
		libpng12-dev \
		libwmf-dev \
		libjasper-dev \
		libgs-dev \
		libmagickwand-dev \
		libssl-dev \
		rsyslog \
		wget \
		nano
		
RUN cpan MIME::Lite \
	Email::MIME \
	MIME::Base64 \
	IO::Socket::SSL \
	App::cpanminus
	
RUN cpanm Authen::SASL

#Add SSL SUPPORT TO MIME::Lite
RUN find /usr/local/share/perl -name Lite.pm -exec sed -i 's/my @_net_smtp_opts = qw( Hello LocalAddr LocalPort Timeout/my @_net_smtp_opts = qw( Hello LocalAddr LocalPort Timeout SSL/g' {} \; 

RUN 	cd /tmp && \
		wget ftp://ftp.imagemagick.org/pub/ImageMagick/ImageMagick.tar.gz && \
		tar xfz ImageMagick.tar.gz && \
		cd ImageMagick-7.0.* && \
		./configure --with-perl=yes --prefix=/usr && \
		make install && \
		ldconfig /usr/local/lib 

RUN 	cd /tmp && \
 		wget http://ftp.de.debian.org/debian/pool/main/z/zbar/zbar_0.10+doc.orig.tar.gz && \
 		tar xzf zbar_0.10+doc.orig.tar.gz && \
 		cd zbar-0.10 && \
 		export CFLAGS="" && \
 		./configure --without-qt --without-gtk --without-python --disable-video && \
 		make install && \
 		cd perl && \
 		perl Makefile.PL && \
 		make install && \
 		ldconfig /usr/local/lib 		

		
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*	

RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8 
RUN echo "Europe/Moscow" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata

ENV DIR="/home/script"	

RUN mkdir -p ${DIR}
RUN mkdir -p ${DIR}/tmp  

COPY barcode_mail_keeper ${DIR}/
RUN chmod +x ${DIR}/barcode_mail_keeper
  
WORKDIR ${DIR}

CMD ["/home/script/barcode_mail_keeper", "docker"]

