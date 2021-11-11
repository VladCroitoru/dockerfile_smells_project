FROM docker/whalesay:latest

RUN apt-get -y update 
RUN apt-get clean && apt-get install -y fortune
RUN apt-get install -y fortune
CMD /usr/games/fortune -a | cowsay

