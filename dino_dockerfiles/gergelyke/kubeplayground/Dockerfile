FROM node:latest
EXPOSE 8080
COPY server.js .
COPY package.json .
CMD npm install

# Must use exec form otherwise node will not get SIGTERM!
CMD ["node", "server.js"]

# DO NOT USE SHELL FORM!

# CMD node server.js