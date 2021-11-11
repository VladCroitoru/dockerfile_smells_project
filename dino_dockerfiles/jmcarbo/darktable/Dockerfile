FROM ubuntu:20.04
LABEL org.opencontainers.image.source https://github.com/jmcarbo/darktable
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update \ 
  && apt-get install -y xrdp software-properties-common 

#RUN apt-get install -y tasksel
#RUN tasksel install ubuntu-mate-desktop
#RUN tasksel install ubuntu-mate-core 

RUN apt-get install -y mate-core mate-desktop-environment mate-notification-daemon 

#RUN apt-get install -y ubuntu-mate-desktop

RUN apt-get install -y libreoffice firefox
RUN apt-get install -y darktable
RUN apt-get install -y wget
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - 
#RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
#RUN sh -c 'echo "deb [arch=arm64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
#RUN apt-get update 
#RUN apt-get install -y  google-chrome-stable

RUN xrdp-keygen xrdp /etc/xrdp/rsakeys.ini

#RUN add-apt-repository -y ppa:pmjdebruijn/darktable-release \
#  && apt-get -y update \
#  && apt-get -y install darktable \
RUN sed -i.bak '/fi/a #xrdp multiple users configuration \n mate-session \n' /etc/xrdp/startwm.sh

EXPOSE 3389

CMD for i in $(seq 1 30); do useradd -m -p $(echo ${USER_PASSWORD:=password} |openssl passwd -1 -stdin) user$i; done && xrdp-sesman && xrdp -nodaemon
