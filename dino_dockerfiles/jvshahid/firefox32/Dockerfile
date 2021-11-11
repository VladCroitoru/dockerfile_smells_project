FROM toopher/ubuntu-i386:12.04
RUN apt-get update
RUN apt-get -y install firefox=11.0+build1-0ubuntu4
RUN apt-get -y install icedtea-plugin
RUN apt-get -y install libxmu-dev
ENV DISPLAY :0
ADD start-firefox /usr/bin/start-firefox
CMD start-firefox
