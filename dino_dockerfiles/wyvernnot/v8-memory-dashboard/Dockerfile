FROM mhart/alpine-node:6.2.0
MAINTAINER wyvernnot <wyvernnot@gmail.com>
ENV WILDDOG_URL=url WILDDOG_SECRET=secret CLIENT_ID=id CLIENT_SECRET=secret MIXPANEL_TOKEN=token
WORKDIR /src
COPY . .
RUN npm install
EXPOSE 8080
CMD ["npm","start"]
