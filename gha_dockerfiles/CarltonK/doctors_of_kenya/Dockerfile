FROM debian:buster

# patch image and download dependencies
RUN apt-get update && apt-get install -y \ 
  wget \
  make \
  curl \
  gnupg \
  software-properties-common \
  procps

# install nodejs @ 10
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -

# Add openjdk-8-jre
RUN wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public | apt-key add -
RUN add-apt-repository --yes https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/

# install node + openjdk
# via https://stackoverflow.com/a/59436618/10362582
RUN apt-get update && apt-get install -y nodejs adoptopenjdk-8-hotspot

# Install global modules
RUN npm install -g nodemon eslint eslint-plugin-import

# download and install firebase CLI
RUN wget -nv -O firebase https://firebase.tools/bin/linux/latest
RUN chmod +x firebase

RUN mv firebase /usr/bin/

# Create dir and copy all content
RUN mkdir -p /app
COPY . /app/

WORKDIR /app

RUN cd functions; npm i

ENTRYPOINT [ "make", "serve-dev" ]