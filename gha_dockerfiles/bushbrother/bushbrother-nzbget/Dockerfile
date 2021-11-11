# Buildstage
FROM lsiobase/alpine:3.9 as buildstage

RUN \
 echo "********************************" && \
 echo "**** Install Build Packages ****" && \
 echo "********************************" && \
 apk add \
	git \
	curl \
	automake \
	make \
	autoconf \
	g++ \
	libtool \
	intltool && \
 echo "************************" && \
 echo "**** Install NZBGet ****" && \
 echo "************************" && \
 mkdir -p /app/nzbget && \
 cd /app/nzbget && \
 wget https://nzbget.net/download/nzbget-latest-bin-linux.run && \
 sh nzbget-latest-bin-linux.run --destdir /app/nzbget && \
 echo "********************************" && \
 echo "**** Initialise nzbget.conf ****" && \
 echo "********************************" && \
 sed -i \
        -e "s#^MainDir=.*#MainDir=/downloads#g" \
        -e "s#^ScriptDir=.*#ScriptDir=$\{MainDir\}/scripts#g" \
        -e "s#^WebDir=.*#WebDir=$\{AppDir\}/webui#g" \
        -e "s#^ConfigTemplate=.*#ConfigTemplate=$\{AppDir\}/webui/nzbget.conf.template#g" \
        -e "s#^UnrarCmd=.*#UnrarCmd=$\{AppDir\}/unrar#g" \
        -e "s#^SevenZipCmd=.*#SevenZipCmd=$\{AppDir\}/7za#g" \
        -e "s#^CertStore=.*#CertStore=$\{AppDir\}/cacert.pem#g" \
        -e "s#^CertCheck=.*#CertCheck=yes#g" \
        -e "s#^DestDir=.*#DestDir=$\{MainDir\}/completed#g" \
        -e "s#^InterDir=.*#InterDir=$\{MainDir\}/intermediate#g" \
        -e "s#^LogFile=.*#LogFile=$\{MainDir\}/nzbget.log#g" \
        -e "s#^AuthorizedIP=.*#AuthorizedIP=127.0.0.1#g" \
 /app/nzbget/nzbget.conf && \
 cp /app/nzbget/nzbget.conf /app/nzbget/webui/nzbget.conf.template && \
 echo "*********************" && \
 echo "**** Symlink git ****" && \
 echo "*********************" && \
 ln -s /usr/bin/git /app/nzbget/git && \
 echo "********************" && \
 echo "**** Init Certs ****" && \
 echo "********************" && \
 touch /app/nzbget/pubkey.pem && \
 curl -o \
	/app/nzbget/cacert.pem -L \
	"https://nzbget.net/info/cacert.pem" && \
 cd .. && \
 echo "**************************************" && \
 echo "**** Make and Install par2cmdline ****" && \
 echo "**************************************" && \
 git clone https://github.com/Parchive/par2cmdline.git && \
 cd par2cmdline && \
 ./automake.sh && \
 ./configure --disable-dependency-tracking && \
 make && \
 make check && \
 make install

# Runtime stage
FROM lsiobase/alpine:3.9

# Set version label
LABEL maintainer="Bushbrother"

# Add local files and files from buildstage
COPY --from=buildstage /app/nzbget /app/nzbget
COPY --from=buildstage /app/par2cmdline/par2 /usr/local/bin
COPY --from=buildstage /app/par2cmdline/man/par2.1 /usr/local/share/man/man1
COPY root/ /

#Main Runtime
RUN \
 echo "***************************" && \
 echo "**** BUSHBROTHER BUILD ****" && \
 echo "***************************" && \
 echo "" && \
 echo "**************************" && \
 echo "**** Install Packages ****" && \
 echo "**************************" && \
 apk add --no-cache \
	curl \
	libxml2 \
	libgomp \
	openssl \
	p7zip \
	python3 \
	unrar \
	ffmpeg \
	git \
	wget && \
 echo "***********************" && \
 echo "**** Symlink files ****" && \
 echo "***********************" && \
 ln -sf /usr/local/bin/par2 /usr/local/bin/par2create && \
 ln -sf /usr/local/bin/par2 /usr/local/bin/par2verify && \
 ln -sf /usr/local/bin/par2 /usr/local/bin/par2repair && \
 ln -sf /usr/bin/python3 /usr/bin/python

# Ports and volumes
VOLUME /config /downloads
EXPOSE 6789
