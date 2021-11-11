FROM maven:3-jdk-8

ADD . /pokemons/

WORKDIR /pokemons

RUN ls -a

RUN mvn clean install

RUN chmod +x /pokemons/src/main/scripts/start.sh

CMD /pokemons/src/main/scripts/start.sh

EXPOSE 8080
EXPOSE 12345

VOLUME /var/log/