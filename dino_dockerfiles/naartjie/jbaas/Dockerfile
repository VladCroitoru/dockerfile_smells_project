FROM mhart/alpine-node:6.0

WORKDIR /src

# http://bit.ly/1QfnlUR
COPY package.json /tmp/package.json
RUN cd /tmp && NODE_ENV=production npm install
RUN cp -a /tmp/node_modules /src/node_modules

COPY . .

EXPOSE 8080
ENV PORT 8080
CMD ["npm", "start"]
