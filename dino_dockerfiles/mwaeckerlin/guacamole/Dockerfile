FROM ubuntu
MAINTAINER mwaeckerlin
ENV TERM xterm

ENV VNC_OPTIONS "-depth 24 -geometry 1280x752"
ENV USERS "test:ert456"
ENV MD5_USERS ""
ENV PACKAGES ""
ENV BASEPATH "/guacamole"

EXPOSE 8080

ADD keyboard /etc/default/keyboard
ADD locale /etc/default/locale
ADD debconf-selections /tmp/debconf-selections

RUN locale-gen --purge de_CH.UTF-8
RUN echo "Europe/Zurich" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen
RUN sed -i -e 's/# de_CH.UTF-8 UTF-8/de_CH.UTF-8 UTF-8/' /etc/locale.gen
RUN dpkg-reconfigure --frontend=noninteractive locales
RUN update-locale LANG=de_CH.UTF-8
RUN debconf-set-selections < /tmp/debconf-selections

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true LC_ALL=C LANGUAGE=C LANG=C apt-get install -y guacamole-tomcat tightvncserver sudo emacs xubuntu-desktop

ADD xstartup /etc/vnc/xstartup
ADD start.sh /start.sh

CMD /start.sh

VOLUME /home
