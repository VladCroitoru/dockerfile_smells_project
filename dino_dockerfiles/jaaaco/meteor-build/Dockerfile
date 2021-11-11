FROM node:4.8.3-slim
RUN apt-get update && apt-get install bzip2 curl -y
RUN npm install pm2 -g
# install Meteor
RUN curl "https://install.meteor.com/?release=1.5" | sh
ENV PORT 80
EXPOSE 80
ENV NODE_ENV production

# add app source
ONBUILD COPY app /app
ONBUILD WORKDIR /app
# build app
ONBUILD RUN meteor npm install && mkdir /build && meteor build --allow-superuser --directory /build && cd /build/bundle/programs/server && npm install

CMD cd /build/bundle && node main.js

