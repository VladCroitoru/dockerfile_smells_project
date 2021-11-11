FROM node:6.17.1

# to help docker debugging
ENV DEBIAN_FRONTEND noninteractive

# install yarn (faster than npm...)
RUN npm config set strict-ssl false
RUN apt-get update && apt-get install -y apt-transport-https
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y yarn

# install nodejs dependencies
WORKDIR /app
COPY ./package.json /app/package.json
RUN yarn install && yarn cache clean

# ezmasterization of istex-ark:
# creates the /etc/ezmaster.json in the docker image.
# It will tell to ezmaster where is your web server (ex: port 3000),
# where is your JSON configuration file,
# and where is your data folder
RUN echo '{ \
  "httpPort": 3000, \
  "configPath": "/app/dump/istexcorpus-arksubpublisher.json", \
  "dataPath": "" \
}' > /etc/ezmaster.json
EXPOSE 3000

# copy source code
COPY . /app

CMD npm start