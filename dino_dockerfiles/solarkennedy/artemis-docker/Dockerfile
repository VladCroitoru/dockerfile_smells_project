FROM ubuntu:trusty
MAINTAINER Kyle Anderson <kyle@xkyle.com>

RUN apt-get update -y
RUN apt-get install -y software-properties-common
RUN /usr/bin/apt-add-repository -y ppa:ubuntu-wine/ppa
RUN dpkg --add-architecture i386
RUN apt-get update -y

RUN apt-get install -y wine1.7
RUN apt-get install -y winetricks
RUN apt-get -y install winbind

RUN apt-get -y install xvfb x11vnc xdotool

ENV WINEPREFIX /root/prefix32
ENV WINEARCH win32
ENV DISPLAY :0

RUN wget http://www.artemis.eochu.com/Artemis_demo_v2_1.exe
RUN winetricks --unattended winxp
ADD install-wrapper.sh /usr/bin/
RUN /usr/bin/install-wrapper.sh
RUN ls -l "/root/prefix32/drive_c/Program Files/Artemis DEMO"
RUN rm /Artemis_demo_v2_1.exe

RUN apt-get -y install imagemagick caca-utils x11-apps
ADD run-wrapper.sh /usr/bin/
EXPOSE 2010
CMD /usr/bin/run-wrapper.sh
