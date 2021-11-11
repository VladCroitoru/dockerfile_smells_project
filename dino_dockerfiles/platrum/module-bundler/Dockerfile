FROM m1nor/docker-node-webpack

ADD ./webpack.config.js /app/webpack.config.js
ADD ./package.json /app/package.json
ADD ./package-lock.json /app/package-lock.json
ADD ./.babelrc /app/.babelrc

RUN [ "npm", "install" ]
