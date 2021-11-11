FROM docker/whalesay:latest
RUN apt-get -y update && apt-get install -y fortunes
CMD echo "How funny is this......"
CMD /usr/games/fortune -a | cowsay
