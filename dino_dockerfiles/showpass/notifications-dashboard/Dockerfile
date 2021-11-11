FROM node:6-alpine

RUN mkdir /app/
WORKDIR /app/

RUN npm install -g gulp

COPY package.json .
RUN npm install

# Build ./dist folder
COPY src/ src/
COPY server.js .
COPY gulpfile.babel.js .
COPY .babelrc .
RUN npm run build

# Remove dev dependencies
RUN npm prune --production
RUN rm -r src/
RUN rm gulpfile.babel.js
RUN rm .babelrc

ENV HOST 0.0.0.0
ENV PORT 4040
ENV NODE_ENV production
EXPOSE $PORT

CMD ["node", "server.js"]
