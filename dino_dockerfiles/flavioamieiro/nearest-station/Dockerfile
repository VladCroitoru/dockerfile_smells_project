FROM ubuntu

RUN apt-get update

RUN apt-get install -y build-essential npm git
RUN ln -s /usr/bin/nodejs /usr/bin/node

RUN mkdir -p /srv

RUN git clone https://github.com/AlertaDengue/nearest-station.git /srv/nearest-station
WORKDIR /srv/nearest-station
RUN npm install

EXPOSE 8000
CMD ["npm", "start"]
