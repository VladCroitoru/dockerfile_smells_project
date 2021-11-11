# Pull base image.
FROM node:0.12.9-slim
MAINTAINER Nimrod Nagy <nimrod.nagy@lynxsolutions.eu>

# Latest Git version
RUN echo "deb http://ftp.us.debian.org/debian testing main contrib non-free" >> /etc/apt/sources.list

# Install git
RUN apt-get update && apt-get install -y git rsync bzip2

# Global install gulp and bower
RUN npm set progress=false && \
	npm install -g gulp grunt bower phantomjs && \
	printf '\n%s' 'registry = http://nexus.lynxsolutions.eu/repository/npm/' >> /root/.npmrc && \
	echo '{ "allow_root": true }' > /root/.bowerrc

# Binary may be called nodejs instead of node
RUN ln -s /usr/bin/nodejs /usr/bin/node

# Define working directory.
WORKDIR /workspace

CMD ["/bin/bash"]
ENTRYPOINT []
