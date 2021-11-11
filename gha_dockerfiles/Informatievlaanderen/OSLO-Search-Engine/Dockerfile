FROM node:lts-alpine

# make the 'app' folder the current working directory
WORKDIR /app

ARG NPM_TOKEN
COPY .npmrc .npmrc

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
RUN npm install
RUN rm -f .npmrc

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN npm run build

FROM djoewie/oslo-simple-server:v0.3.0

COPY --from=0 /app/dist /usr/src/app/dist

#for testing purpose
#COPY --from=0 /app/dist /usr/src/app/dist/tools/search-engine
