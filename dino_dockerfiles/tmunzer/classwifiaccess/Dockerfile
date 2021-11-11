FROM node:6-wheezy
LABEL fr.ah-lab.classwifiaccess.version="0.0.3"
LABEL fr.ah-lab.classwifiaccess.release-date="2017-03-11"

RUN npm install -g bower

COPY ./src /app/

WORKDIR /app

RUN npm	install	&& bower install --allow-root


EXPOSE 51367
ENTRYPOINT /app/docker-entrypoint.sh 51367

