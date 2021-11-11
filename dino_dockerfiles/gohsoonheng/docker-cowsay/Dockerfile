FROM debian:jessie

RUN apt-get update && apt-get install -y cowsay
COPY docker.cow /usr/share/cowsay/cows/docker.cow

ENTRYPOINT ["/usr/games/cowsay","-f","docker"]
CMD ["moby","dock"]
