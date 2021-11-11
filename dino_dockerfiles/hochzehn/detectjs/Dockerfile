FROM node:6.2.0
MAINTAINER Jan Papenbrock <j.papenbrock@hochzehn.com>

WORKDIR /opt/app

ADD package.json /opt/app/
RUN npm install

ADD . /opt/app/
RUN npm install
RUN npm link

ENTRYPOINT ["detectjs"]
CMD [""]
