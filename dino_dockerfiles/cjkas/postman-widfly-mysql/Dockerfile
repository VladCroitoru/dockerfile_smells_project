FROM cjkas/maven-oracle-jdk:jdk8

RUN apt-get update

RUN apt-get install -y mysql-server gnupg2 
RUN wget -q https://deb.nodesource.com/setup_6.x && chmod +x setup_6.x && ./setup_6.x
RUN apt-get install -y nodejs build-essential libssl-dev
RUN npm install -g newman

RUN node -v
RUN npm -v
RUN newman -v
RUN rm -fr /var/lib/apt/lists/*

WORKDIR /tmp

CMD [ "/bin/bash", "-l"]
EXPOSE 8080