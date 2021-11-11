FROM ubuntu

RUN apt-get update -qq
RUN apt-get install -qqy firefox
RUN apt-get install -qqy wmctrl xdotool
ADD ./loop.sh /code/loop.sh
WORKDIR /code
ENTRYPOINT ./loop.sh
