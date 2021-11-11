FROM ubuntu
RUN apt-get update
RUN apt-get install -y wget
RUN wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | apt-key add -
RUN echo "deb https://download.sublimetext.com/ apt/stable/" |  tee /etc/apt/sources.list.d/sublime-text.list
RUN apt-get install -y apt-transport-https
RUN apt-get update
RUN apt-get install -y sublime-text
RUN apt-get install -y libgtk2.0-0
RUN apt-get install -y libcanberra-gtk-module
ENTRYPOINT /usr/bin/subl
