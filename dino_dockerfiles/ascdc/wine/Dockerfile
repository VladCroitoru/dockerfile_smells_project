FROM ascdc/cron
MAINTAINER  ASCDC <asdc.sinica@gmail.com>

ADD run.sh /run.sh	
ADD set_root_pw.sh /set_root_pw.sh	
ADD locale.gen /etc/locale.gen
ADD locale-archive /usr/lib/locale/locale-archive


RUN chmod +x /*.sh && \
	apt-get update && \
	apt-get install -y software-properties-common && \
	add-apt-repository -y ppa:ubuntu-wine/ppa && \	
	dpkg --add-architecture i386 && \
	apt-get update && \
	apt-get install -y wine1.8 && \
	apt-get install -y winetricks xvfb && \
	export DISPLAY=:0.0 && \
	apt-get install -y openssh-server pwgen vim && \
	sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config && \
	mkdir -p /var/run/sshd &&  \
	sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && \
	sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && \
	sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config && \
	echo "X11UseLocalhost yes" >> /etc/ssh/sshd_config && \
	echo "alias ll='ls -al'" >> /root/.profile && \
	apt-get install -y locales && \
	locale-gen zh_TW.UTF-8 && \
	DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales && \ 
	locale-gen zh_TW.UTF-8 && \
	echo "export LANG=zh_TW.UTF-8" >> /root/.profile && \ 
	echo "export LANGUAGE=zh_TW" >> /root/.profile && \
	echo "export LC_ALL=zh_TW.UTF-8" >> /root/.profile && \
	apt-get install -y build-essential && \
	apt-get -y dist-upgrade && \
	apt-get install -y byobu htop man unzip xrdp xfce4 && \
	echo xfce4-session >~/.xsession && \
	mkdir -p /etc/java && \ 
	wget -P /etc/java/ --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u102-b14/jdk-8u102-linux-x64.tar.gz && \
	tar zxvf /etc/java/jdk-8u102-linux-x64.tar.gz -C /etc/java && \
	chown -R root:root /etc/java && \
	echo "export JAVA_HOME=/etc/java/jdk1.8.0_102" >> /root/.profile && \
	echo "export PATH=$PATH:$JAVA_HOME/bin" >> /root/.profile 

ENV AUTHORIZED_KEYS **None**

EXPOSE 22
EXPOSE 3389

ENTRYPOINT ["/run.sh"]