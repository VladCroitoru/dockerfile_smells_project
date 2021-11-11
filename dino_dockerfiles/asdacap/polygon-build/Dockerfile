FROM ubuntu:16.04
RUN dpkg --add-architecture i386
RUN apt-get update
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections
RUN apt-get install -y wine build-essential default-jdk
RUN apt-get install -y texlive-latex-extra texlive-lang-cyrillic texlive-fonts-recommended texlive-generic-recommended --no-install-recommends
WORKDIR /contest/
CMD chmod +x -R . && /contest/doall.sh
