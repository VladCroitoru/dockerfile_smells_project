FROM debian:buster-slim
RUN apt-get update && \
    apt-get install -y cowsay && \
    apt-get clean
COPY dragonfire.cow /usr/share/cowsay/cows/
ENTRYPOINT [ "/usr/games/cowthink", "-f", "dragonfire" ]
CMD [ "Dragon Fire!!!!" ]
