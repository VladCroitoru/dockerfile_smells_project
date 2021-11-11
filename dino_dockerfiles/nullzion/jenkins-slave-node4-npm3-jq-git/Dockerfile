FROM evarga/jenkins-slave
MAINTAINER filip@devzion.xyz

# install dependencies
RUN apt-get update
RUN apt-get install -y git jq wget xz-utils build-essential python maven

# install node 4
RUN wget https://nodejs.org/dist/v4.4.4/node-v4.4.4-linux-x64.tar.xz -P /tmp
RUN tar -C /usr/local --strip-components 1 -xJf /tmp/node-v4.4.4-linux-x64.tar.xz

# update npm to version 3
RUN npm install -g npm@3
