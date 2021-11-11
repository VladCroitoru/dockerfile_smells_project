FROM ubuntu:14.04

MAINTAINER m.maatkamp@gmail.com version: 0.1

# ---
# crosstool-NG
#  see https://github.com/marcelmaatkamp/crosstool-NG

RUN \
 apt-get update && \
 apt-get dist-upgrade -y && \
 apt-get install -y git autoconf build-essential gperf bison flex texinfo libtool libncurses5-dev wget gawk libc6-dev python-serial libexpat-dev unzip libtool

RUN \
 mkdir /home/swuser && \
 groupadd -r swuser -g 433  && \
 useradd -u 431 -r -g swuser -d /home/swuser -s /sbin/nologin -c "Docker image user" swuser  && \
 chown -R swuser:swuser /home/swuser && \
 adduser swuser sudo && \
 echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

WORKDIR /opt/Espressif
RUN chown -R swuser /opt/Espressif
USER swuser

RUN git clone -b lx106 git://github.com/jcmvbkbc/crosstool-NG.git 

WORKDIR /opt/Espressif/crosstool-NG

RUN \
 ./bootstrap && ./configure --prefix=`pwd` && make && sudo make install && \
 ./ct-ng xtensa-lx106-elf && \
 ./ct-ng build

ENV PATH .:/opt/Espressif/crosstool-NG/builds/xtensa-lx106-elf/bin:/opt/Espressif/esptool-ck:$PATH

ENV ESP_IOT_SDK_MAJOR_VERSION 1.2.0
ENV ESP_IOT_SDK_MINOR_VERSION 15_07_03
ENV ESP_IOT_SDK_VERSION $ESP_IOT_SDK_MAJOR_VERSION'_'$ESP_IOT_SDK_MINOR_VERSION

WORKDIR /opt/Espressif
RUN \
 wget -O esp_iot_sdk_v$ESP_IOT_SDK_VERSION.zip https://github.com/esp8266/esp8266-wiki/raw/master/sdk/esp_iot_sdk_v$ESP_IOT_SDK_VERSION.zip && \
 unzip esp_iot_sdk_v$ESP_IOT_SDK_VERSION.zip && \
 mv esp_iot_sdk_v$ESP_IOT_SDK_MAJOR_VERSION ESP8266_SDK && \
 mv License ESP8266_SDK && \
 rm esp_iot_sdk_v$ESP_IOT_SDK_VERSION.zip

WORKDIR /opt/Espressif/crosstool-NG/builds/xtensa-lx106-elf/bin
RUN for i in `ls`; do  filename=`echo $i|sed -e 's/xtensa-lx106-elf-//'`; sudo ln -s xtensa-lx106-elf-$filename /opt/Espressif/crosstool-NG/builds/xtensa-lx106-elf/bin/xt-$filename; done && \
    sudo ln -s /opt/Espressif/crosstool-NG/builds/xtensa-lx106-elf/bin/xtensa-lx106-elf-gcc /opt/Espressif/crosstool-NG/builds/xtensa-lx106-elf/bin/xt-xcc

WORKDIR /opt/Espressif/ESP8266_SDK
RUN sed -i -e 's/xt-ar/xtensa-lx106-elf-ar/' -e 's/xt-xcc/xtensa-lx106-elf-gcc/' -e 's/xt-objcopy/xtensa-lx106-elf-objcopy/' Makefile && \
 mv examples/IoT_Demo .

RUN wget -O lib/libc.a https://github.com/esp8266/esp8266-wiki/raw/master/libs/libc.a && \
 wget -O lib/libhal.a https://github.com/esp8266/esp8266-wiki/raw/master/libs/libhal.a && \
 wget -O include.tgz https://github.com/esp8266/esp8266-wiki/raw/master/include.tgz && \
 tar -xvzf include.tgz

WORKDIR /opt/Espressif
RUN git clone https://github.com/tommie/esptool-ck.git && \
    cd esptool-ck && make && sudo cp esptool /usr/bin

RUN git clone https://github.com/themadinventor/esptool esptool-py && \
    sudo ln -s $PWD/esptool-py/esptool.py crosstool-NG/builds/xtensa-lx106-elf/bin/

ENV CPATH /opt/Espressif/ESP8266_SDK/include
ENV LD_LIBRARY_PATH /opt/Espressif/ESP8266_SDK/lib
RUN export 

# Examples:
#  https://github.com/esp8266/esp8266-wiki/wiki/Building

WORKDIR /opt/Espressif/ESP8266_SDK
RUN make 

WORKDIR /opt/Espressif
RUN git clone https://github.com/esp8266/source-code-examples.git && \
    ln -s /opt/Espressif/ESP8266_SDK/esp_iot_sdk_v0.9.3/ld  /opt/Espressif/source-code-examples/ld && \
    cd source-code-examples/blinky && sed -i -e '5ivoid user_rf_pre_init(void) { }\' user/user_main.c && make

# WORKDIR /opt/Espressif/ESP8266_SDK
# RUN wget -O at_v0.20_14_11_28.zip https://github.com/esp8266/esp8266-wiki/raw/master/sdk/at_v0.20_14_11_28.zip
# RUN unzip at_v0.20_14_11_28.zip && rm -rf at_v0.20_14_11_28.zip
# RUN cd at_v0.20_on_SDKv0.9.3 && for i in `ls at`; do mv at/$i .; done && make 

WORKDIR /opt/Espressif/ESP8266_SDK/IoT_Demo
RUN make
WORKDIR /opt/Espressif/ESP8266_SDK/IoT_Demo/.output/eagle/debug/image
RUN esptool -eo eagle.app.v6.out -bo eagle.app.v6.flash.bin -bs .text -bs .data -bs .rodata -bc -ec && \
    xtensa-lx106-elf-objcopy --only-section .irom0.text -O binary eagle.app.v6.out eagle.app.v6.irom0text.bin && \
    cp eagle.app.v6.flash.bin ../../../../../bin/ && \
    cp eagle.app.v6.irom0text.bin ../../../../../bin/ 

WORKDIR /opt/Espressif/ESP8266_SDK/include/xtensa
RUN wget https://raw.githubusercontent.com/espressif/esp_iot_rtos_sdk/master/extra_include/xtensa/simcall-fcntl.h && \
    wget https://raw.githubusercontent.com/espressif/esp_iot_rtos_sdk/master/extra_include/xtensa/simcall-errno.h

WORKDIR /opt/Espressif
RUN git clone https://github.com/nodemcu/nodemcu-firmware.git
WORKDIR /opt/Espressif/nodemcu-firmware
RUN sed -i -e 's/#if __XTENSA_WINDOWED_ABI__/#ifdef __XTENSA_WINDOWED_ABI__/g' /opt/Espressif/ESP8266_SDK/include/machine/setjmp.h && \
    sed -i -e 's/#define EFAULT 14/\/\/ #define EFAULT 14/g' app/include/arch/cc.h && \
    ln -s /opt/Espressif/ESP8266_SDK/lib/libhal.a lib && \
    ln -s /opt/Espressif/ESP8266_SDK/lib/libc.a lib/
RUN make

WORKDIR /opt/Espressif
