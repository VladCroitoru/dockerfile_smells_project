FROM debian:latest

RUN apt-get update && apt-get install -y --no-install-recommends \ 
  cowsay

RUN mv /usr/share/cowsay/cows/default.cow /usr/share/cowsay/cows/cow.cow

COPY docker.cow /usr/share/cowsay/cows/

RUN ln -sv /usr/share/cowsay/cows/docker.cow /usr/share/cowsay/cows/default.cow

ENV PATH $PATH:/usr/games

CMD ["cowsay"]
