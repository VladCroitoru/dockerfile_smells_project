FROM turnkeylinux/core-13.0
RUN dpkg --add-architecture i386
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install imagemagick -y
RUN apt-get install libc6:i386 -y 


RUN mkdir /home/armcompiler
WORKDIR /home/armcompiler
RUN wget http://static.leaflabs.com/pub/codesourcery/gcc-arm-none-eabi-latest-linux32.tar.gz
RUN tar xzvf gcc-arm-none-eabi-latest-linux32.tar.gz
ENV PATH $PATH:/home/armcompiler/arm/bin
RUN mkdir /home/source
WORKDIR /home/source
RUN git clone https://github.com/sonomasoft/onyxfirmware.git
WORKDIR /home/source/onyxfirmware
RUN git checkout master

RUN apt-get -y install build-essential g++ curl libssl-dev apache2-utils git libxml2-dev
#WORKDIR /home/source/onyxfirmware/firmware_loader
#RUN make
RUN apt-get install usbutils -y
RUN apt-get install sudo -y
#WORKDIR /home/source/onyxfirmware/firmware
ENTRYPOINT lsusb && git pull && cd firmware_loader && make && cd ../firmware && make upload
