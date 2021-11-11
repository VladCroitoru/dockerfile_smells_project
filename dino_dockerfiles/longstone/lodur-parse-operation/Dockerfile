FROM node:alpine
EXPOSE 8080
# copy app to src
ADD . /script
WORKDIR /script
ENV NODE_ENV=production
RUN npm ci && npm run-script heroku-postbuild && rm -rf node_modules
ENTRYPOINT npm run-script start

