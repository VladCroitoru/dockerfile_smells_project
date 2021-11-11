# scratch
FROM node:16-alpine
WORKDIR /app
#RUN cat ~/.npmrc > ~/.npmrc
COPY package-lock.json package.json ./
#RUN npm i
RUN echo $PWD
#COPY docs ./docs
#COPY babel.config.js .
COPY .eslintrc.js .
COPY .eslintignore .
COPY webpack.config.server.js .
#COPY webpack.config.client.ts .
COPY rollup.config.ts .
COPY rollup.config.functions.ts .
COPY lerna.json .
COPY styleguide.config.js .
COPY tsconfig.json .
# mayb delete it - not using
#COPY rollup.config.server.ts .
