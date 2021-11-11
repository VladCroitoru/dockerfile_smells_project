FROM debian

WORKDIR /app

RUN apt-get -qq update
RUN apt-get -qq -y install curl

RUN curl -L "https://cli.run.pivotal.io/stable?release=linux64-binary&source=github" | tar -zx

RUN chmod +x cf
RUN mv cf /usr/bin/
