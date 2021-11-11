FROM readytalk/nodejs

WORKDIR /app
ADD . /app
RUN npm install
EXPOSE 80
ENTRYPOINT ["/nodejs/bin/npm", "start"]
