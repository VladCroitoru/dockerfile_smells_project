FROM ubuntu:latest

RUN apt-get update && apt-get -y install software-properties-common
RUN add-apt-repository -y ppa:mystic-mirage/pycharm
RUN apt-get update && apt-get -y install git pycharm-community

VOLUME ["/root/.PyCharmCE2016.3"]

CMD "pycharm-community"