FROM node:14.17-alpine as build

ARG BPC_URL=''
ARG BPP_URL=''
ARG PM_URL=''
ARG NODE_ENV=production
ENV BPC_URL=${BPC_URL}
ENV BPP_URL=${BPP_URL}
ENV PM_URL=${PM_URL}
ENV NODE_ENV=${NODE_ENV}

WORKDIR /build
ENV PATH=$PATH:/build/node_modules/.bin
ENV NODE_ENV=development

ADD package.json .
ADD package-lock.json .

# Installing packages
RUN npm ci

# Building the client
ADD .babelrc .
ADD ./client ./client
ADD webpack.config.js .
RUN webpack


FROM node:14.17-alpine

ENV NODE_ENV=production
# Set the working directory.
WORKDIR /bpc_console

# Copying the code into image. Be aware no config files are including.
COPY --from=build /build/client ./client
ADD package.json .
ADD package-lock.json .

# Installing packages
RUN npm i --production
RUN node -e "(async () => {require('geolite2-redist').downloadDbs('./server/$GEO_DBS_DIRECTORY')})()"

ADD ./server ./server

# Exposing our endpoint to Docker.
EXPOSE  8000

# When starting a container with our image, this command will be run.
CMD ["node", "server/index.js"]
