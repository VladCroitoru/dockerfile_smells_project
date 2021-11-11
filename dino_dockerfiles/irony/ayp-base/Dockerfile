FROM dockerfile/nodejs
ADD ./package.json /usr/src/app/package.json
WORKDIR /usr/src/app

RUN ["npm", "install", "--production", "-g"]

# replace this with your main "server" script file
CMD ["node", "index.js"]