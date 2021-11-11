FROM node:argon-slim
RUN npm i pm2 -g --loglevel=verbose
EXPOSE 80
EXPOSE 443
EXPOSE 5001
WORKDIR /usr/src/app
# By taking the package.json seperately,
# the heavy 
COPY package.json /usr/src/app/package.json
RUN npm i --loglevel=verbose
COPY . /usr/src/app

# It doesn't really matter if the code is linted
RUN npm test

CMD pm2 start bin/open-github-teams; pm2 logs 0