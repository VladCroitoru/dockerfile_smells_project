FROM node:8.9.3-alpine
LABEL maintainer="Partner Ecosystem Team, IBM Digital Business Group <imcloud@ca.ibm.com>"

# Build time variable
RUN mkdir /app
WORKDIR /app

ADD . /app

# Install app dependencies
RUN yarn install

ENV PORT 80

EXPOSE 80

CMD [ "yarn", "start" ]
