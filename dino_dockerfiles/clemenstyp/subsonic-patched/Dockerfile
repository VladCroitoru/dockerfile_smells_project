FROM ubuntu:14.04
#CMDBUILD	docker build -t ulikoenig/subsonic_patched https://raw.githubusercontent.com/ulikoenig/subsonic-patched/master/Dockerfile
#CMDRUN		docker run -d --net=host -p 4040:4040 -p 9412:9412 -v /var/lib/subsonic:/data:rw -v /mnt/harddrive/Medien:/Medien:ro  ulikoenig/subsonic_patched

MAINTAINER Uli König <docker@ulikoenig.de.nospam> (@u98)

ENV	JAVA_HOME /usr/lib/jvm/java-8-oracle

ENV	LANG	de_DE.UTF-8
ENV	LC_ALL	de_DE.UTF-8
ENV	LANGUAGE	de_DE

RUN	apt-get update && \
#Flac, Lame, FFMPEG, Oracle Java JDK
	apt-get install -y language-pack-de && \
	update-locale LANG=de_DE.UTF-8 && \
	update-locale LANGUAGE=de_DE && \
	locale-gen && \
	apt-get install -y software-properties-common python-software-properties flac lame && \
	add-apt-repository -y ppa:mc3man/trusty-media && \
	echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
	add-apt-repository -y ppa:webupd8team/java && \
	apt-get update && \
	apt-get install -y oracle-java8-installer ffmpeg maven git lintian fakeroot && \
#Download Sources from Git
	git clone git://github.com/Libresonic/libresonic.git && \
	cd /libresonic && \
	git checkout stable && \
#Build Sources from Scratch
	mvn package && \
	mvn -P full -pl libresonic-booter -am install && \
	mvn -P full -pl libresonic-installer-debian/ -am install && \
#Install Subsonic
	dpkg -i ./libresonic-installer-debian/target/libresonic-*.deb && \
#Remove unnecessary files
	rm -r -f /libresonic /root/.m2 && \
	apt-get purge -y maven git lintian fakeroot software-properties-common python-software-properties && \
	apt-get autoremove -y && \
 	apt-get clean && \
	rm -rf /var/lib/apt/lists/* && \
	rm -rf /var/cache/oracle-jdk8-installer 

RUN	mv /var/libresonic /var/libresonic.default && \
	ln -s /data /var/libresonic 

# Don't fork to the background
RUN	sed -i "s/ > \${LOG} 2>&1 &//" /usr/share/libresonic/libresonic.sh 

#RUN	sed -i "17d" /etc/default/libresonic && \
#	sed -i "i1SUBSONIC_ARGS=\"--port=4040 --https-port=4443 --max-memory=200\"" /etc/default/libresonic

VOLUME	["/data"]
VOLUME	["/Media"]
EXPOSE	4040
EXPOSE	9412

ADD	start.sh /start.sh

#ADD	unionfs.sh /unionfs.sh 
#RUN	sed -i "3i/unionfs.sh" /start.sh

RUN	chmod a+x /start.sh 
CMD	["/start.sh"]
