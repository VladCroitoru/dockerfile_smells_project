
FROM node:5.4
MAINTAINER Rogier Slag

EXPOSE 8080

RUN groupadd -r luser && useradd -r -g luser luser

RUN mkdir /service
ADD package.json /service/
RUN cd /service && npm install
ADD index.js /service/

USER luser
WORKDIR /service
CMD ["node", "index.js"]
