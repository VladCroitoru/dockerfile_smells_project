FROM docker/whalesay:latest

RUN apt-get -y update && apt-get install -y fortunes

ADD README.md /README.md

CMD /usr/games/fortune -a | cowsay
