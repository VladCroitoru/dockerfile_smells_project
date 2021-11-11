FROM ubuntu:16.04
RUN apt-get update && apt-get install -y curl apt-transport-https build-essential \
  && curl -sL https://deb.nodesource.com/setup_8.x | bash - \
  && apt-get install -y nodejs openjdk-8-jdk maven \
  && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
  && echo "deb https://dl.yarnpkg.com/debian/ stable main" \
  | tee /etc/apt/sources.list.d/yarn.list \
  && apt-get update && apt-get install -y yarn
RUN yarn global add http-server
EXPOSE 3000
EXPOSE 8080
WORKDIR /opt/nasa-path-finder
COPY package.json /opt/nasa-path-finder/package.json
COPY yarn.lock /opt/nasa-path-finder/yarn.lock
RUN yarn
COPY . /opt/nasa-path-finder
RUN yarn build
RUN yarn compile
CMD yarn start:web & yarn start:server
