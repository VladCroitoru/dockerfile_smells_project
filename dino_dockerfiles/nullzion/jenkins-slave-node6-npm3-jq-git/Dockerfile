FROM evarga/jenkins-slave
MAINTAINER filip@devzion.xyz

# install dependencies
RUN apt-get update
RUN apt-get install -y git jq wget xz-utils build-essential python autoconf libpng-dev

# install node 4
RUN wget https://nodejs.org/dist/v6.10.3/node-v6.10.3-linux-x64.tar.xz -P /tmp
RUN tar -C /usr/local --strip-components 1 -xJf /tmp/node-v6.10.3-linux-x64.tar.xz

# update npm to version 3
RUN npm update -g npm@3
