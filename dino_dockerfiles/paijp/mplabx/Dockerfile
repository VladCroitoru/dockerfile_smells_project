FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive

RUN set -x &&\
	dpkg --add-architecture i386 &&\
	apt-get update -yq

RUN set -x &&\
	apt-get install -yq --no-install-recommends curl libc6:i386 libx11-6:i386 libxext6:i386 libstdc++6:i386 libexpat1:i386 libxext6 libxrender1 libxtst6 libgtk2.0-0 libxslt1.1
	
RUN set -x &&\
	apt-get install -yq wget
	
RUN set -x &&\
	cd /tmp &&\
	wget --no-check-certificate 'https://ww1.microchip.com/downloads/en/DeviceDoc/MPLABX-v3.35-linux-installer.tar' &&\
	wget --no-check-certificate 'https://ww1.microchip.com/downloads/en/DeviceDoc/xc8-v1.30-linux.run.tar' &&\
	wget --no-check-certificate 'https://ww1.microchip.com/downloads/en/DeviceDoc/xc8-v1.38-full-install-linux-installer.run' &&\
	wget --no-check-certificate 'https://ww1.microchip.com/downloads/en/DeviceDoc/xc16-v1.26-full-install-linux-installer.run' &&\
	wget --no-check-certificate 'https://ww1.microchip.com/downloads/en/DeviceDoc/xc32-v1.42-full-install-linux-installer.run'

RUN set -x &&\
	cd /tmp &&\
	tar xf MPLABX-v3.35-linux-installer.tar &&\
	rm MPLABX-v3.35-linux-installer.tar &&\
	USER=root ./MPLABX-v3.35-linux-installer.sh --nox11 -- --unattendedmodeui none --mode unattended &&\
	rm MPLABX-v3.35-linux-installer.sh

RUN set -x &&\
	cd /tmp &&\
	tar xf xc8-v1.30-linux.run.tar &&\
	chmod a+x xc*.run &&\
	./xc8-v1.30-linux.run --mode unattended --unattendedmodeui none --netservername localhost &&\
	./xc8-v1.38-full-install-linux-installer.run --mode unattended --unattendedmodeui none --netservername localhost --LicenseType FreeMode &&\
	./xc16-v1.26-full-install-linux-installer.run --mode unattended --unattendedmodeui none --netservername localhost --LicenseType FreeMode &&\
	./xc32-v1.42-full-install-linux-installer.run --mode unattended --unattendedmodeui none --netservername localhost --LicenseType FreeMode &&\
	rm xc*.run

RUN set -x &&\
	apt-get install -yq make
	
COPY makefile test.asm /root/

CMD cd&&make build

