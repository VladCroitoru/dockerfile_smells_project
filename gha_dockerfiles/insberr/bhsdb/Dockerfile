FROM nikolaik/python-nodejs
WORKDIR /usr/src/app
COPY . .
RUN yarn install --inline-builds
RUN yarn build
ENTRYPOINT [ "yarn","start" ]
