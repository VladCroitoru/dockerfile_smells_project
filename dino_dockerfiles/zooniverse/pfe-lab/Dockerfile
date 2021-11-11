FROM node:14

WORKDIR /src
RUN chown -R node:node /src

USER node

ADD package.json /src/
ADD package-lock.json /src/

RUN npm install --unsafe-perm

ADD . /src/

CMD ["npm", "start"]
