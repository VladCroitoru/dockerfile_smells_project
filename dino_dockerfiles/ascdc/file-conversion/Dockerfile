FROM ubuntu:trusty
MAINTAINER ASCDC <asdc.sinica@gmail.com>

ADD run.sh /script/run.sh
ADD command.sh /script/command.sh
ADD set_root_pw.sh /script/set_root_pw.sh
ADD locale.gen /etc/locale.gen
ADD locale-archive /usr/lib/locale/locale-archive	

RUN chmod +x /script/*.sh && \
	apt-get update && \
	DEBIAN_FRONTEND=noninteractive && \
	apt-get -y install software-properties-common python-software-properties cron mariadb-client-5.5 vim bc && \
	locale-gen en_US.UTF-8 && \
	export LANG=en_US.UTF-8 && \
	add-apt-repository -y ppa:ondrej/php && \
	add-apt-repository -y ppa:mc3man/trusty-media && \
	apt-add-repository ppa:stebbins/handbrake-snapshots && \
	apt-get update && \
	apt-get -y dist-upgrade && \
	apt-get install -y ffmpeg flac shntool libav-tools imagemagick sox tofrodos unrar-free p7zip-full php7.0-cli php7.0-mysql mediainfo build-essential handbrake-cli exiftool && \
	echo "SHELL=/bin/sh"> /etc/crontab && \
	echo "PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin">> /etc/crontab && \
	echo "*/1 * * * * root /script/command.sh">> /etc/crontab && \
	apt-get install -y subversion build-essential libxvidcore4 zlib1g-dbg zlib1g-dev openssh-server pwgen rsync && \
	svn co https://svn.code.sf.net/p/gpac/code/trunk/gpac gpac && cd gpac && \
	./configure --disable-opengl --use-js=no --use-ft=no --use-jpeg=no --use-png=no --use-faad=no --use-mad=no --use-xvid=no --use-ffmpeg=no --use-ogg=no --use-vorbis=no --use-theora=no --use-openjpeg=no && make && make install && cp bin/gcc/libgpac.so /usr/lib && \
	mkdir -p /var/run/sshd && \
	sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && \
	sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && \
	sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config && \
	apt-get install -y locales && \
	locale-gen zh_TW.UTF-8 && \
	DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales && \ 
	locale-gen zh_TW.UTF-8 && \
	echo "export LANG=zh_TW.UTF-8" >> /root/.profile && \ 
	echo "export LANGUAGE=zh_TW" >> /root/.profile && \
	echo "export LC_ALL=zh_TW.UTF-8" >> /root/.profile && \
	echo "LC_CTYPE=zh_TW.UTF-8" >> /etc/environment && \
	echo "LC_MESSAGES=zh_TW.UTF-8" >> /etc/environment  && \
	echo "LC_TIME=zh_TW.UTF-8" >> /etc/environment  && \
	cd /usr/src && \
	wget ftp://ftp.ruby-lang.org/pub/ruby/1.8/ruby-1.8.6.tar.bz2 && \
	tar xvjf ruby-1.8.6.tar.bz2 && \
	cd ruby-1.8.6 && \
	sed -i 's/elif define(ERANGE)/elif defined(ERANGE)/g'  math.c && \
	./configure;make;make install && \
	cd /usr/src && \
	wget ftp://sourceforge.mirrorservice.org/sites/download.salixos.org/i486/extra-14.2/source/multimedia/flvtool2/flvtool2-1.0.6.tgz && \
	tar xzf flvtool2-1.0.6.tgz && \
	cd flvtool2-1.0.6 && \
	/usr/local/bin/ruby setup.rb config && \
	/usr/local/bin/ruby setup.rb setup && \
	/usr/local/bin/ruby setup.rb install


ENV AUTHORIZED_KEYS **None**
EXPOSE 22

WORKDIR /script
ENTRYPOINT ["/script/run.sh"]
