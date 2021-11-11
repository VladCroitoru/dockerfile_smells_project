FROM node:10.15
MAINTAINER Rogier Slag

EXPOSE 7070

RUN groupadd -r luser && useradd -r -g luser luser
RUN mkdir -p /home/luser/.pm2/
RUN chown -R luser.luser /home/luser
RUN yarn global add pm2

RUN mkdir /service
ADD .babelrc /service/
ADD yarn.lock /service/
ADD package.json /service/
RUN cd /service && yarn install --pure-lockfile
ADD src /service/src/
RUN cd /service && yarn build

USER luser
WORKDIR /service/build/src
CMD ["/usr/local/bin/pm2-docker", "start", "index.js", "--instances=max"]

