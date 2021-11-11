FROM ubuntu
MAINTAINER Matt Koski <maccam912@gmail.com>

RUN apt-get update && apt-get upgrade -y
RUN apt-get install wget software-properties-common python-software-properties build-essential -y

RUN wget -q -O - https://apt.mopidy.com/mopidy.gpg | sudo apt-key add -

RUN wget -q -O /etc/apt/sources.list.d/mopidy.list https://apt.mopidy.com/mopidy.list

RUN add-apt-repository ppa:fatgerman-m/rompr

RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee /etc/apt/sources.list.d/mongodb.list

RUN apt-get update && apt-get upgrade -y

RUN apt-get install git python build-essential wget screen tmux curl vim mongodb-org mopidy mopidy* mpd-client-rompr -y --force-yes

RUN mkdir /root/.config/ && mkdir /root/.config/mopidy/ && cd /root/.config/mopidy && wget https://raw.githubusercontent.com/maccam912/docker-mopidy/master/mopidy.conf

RUN apt-get install python-setuptools python-dev build-essential -y

RUN sudo easy_install pip

RUN sudo pip install --upgrade virtualenv 

RUN sudo pip install Mopidy-Moped
RUN sudo pip install Mopidy-Youtube
RUN sudo pip install Mopidy-SoundCloud
RUN sudo pip install Mopidy-SomaFM
RUN sudo pip install Mopidy-VKontakte
RUN sudo pip install Mopidy-TuneIn
RUN sudo pip install Mopidy-LeftAsRain
RUN sudo pip install mopidy-gmusic
RUN sudo pip install Mopidy-Youtube


CMD ["mopidy"]

EXPOSE 80:80
EXPOSE 443:443
EXPOSE 3000:3000
EXPOSE 6600:6600
EXPOSE 6680:6680
