FROM jrei/systemd-ubuntu:20.04

RUN apt-get update

RUN apt-get -y install curl gnupg

RUN apt-get install g++ build-essential --yes

RUN apt-get install wget
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install ./google-chrome*.deb --yes

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt -y install nodejs

RUN mkdir app
WORKDIR /app

COPY ./_code /app
RUN npm install --production

COPY ./entrypoint.sh /
RUN chmod 555 /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]