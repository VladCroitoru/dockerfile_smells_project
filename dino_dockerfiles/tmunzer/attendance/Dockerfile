FROM node:6-wheezy
LABEL fr.ah-lab.attendance.version="0.0.3"
LABEL fr.ah-lab.attendance.release-date="2017-03-11"

RUN npm install -g bower

COPY ./src /app/

WORKDIR /app

RUN npm	install

RUN groupadd -r ah && useradd -mr -g ah ah
USER ah

EXPOSE 51368
ENTRYPOINT /app/docker-entrypoint.sh 51368

