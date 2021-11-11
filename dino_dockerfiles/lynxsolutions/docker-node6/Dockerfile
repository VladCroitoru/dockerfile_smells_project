# Pull base image.
FROM node:6-slim
MAINTAINER Nimrod Nagy <nimrod.nagy@lynxsolutions.eu>

RUN apt-get update && apt-get install -y apt-transport-https libpng12-dev

# Add yarn to sources list
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

# Latest Git version
RUN echo "deb http://ftp.us.debian.org/debian testing main contrib non-free" >> /etc/apt/sources.list

# Install git
RUN apt-get update && apt-get install -y git rsync bzip2  yarn=0.23.2-1 \
    && rm -r /var/lib/apt/lists/*

# Global install gulp and bower
RUN npm set progress=false && \
	npm install -g gulp grunt bower phantomjs @angular/cli && \
	printf '\n%s' 'registry = http://nexus.lynxsolutions.eu/repository/npm/' >> /root/.npmrc && \
	echo '{ "allow_root": true }' > /root/.bowerrc

# Binary may be called nodejs instead of node
RUN ln -s /usr/bin/nodejs /usr/bin/node

# Define working directory.
WORKDIR /workspace

CMD ["/bin/bash"]
ENTRYPOINT []
