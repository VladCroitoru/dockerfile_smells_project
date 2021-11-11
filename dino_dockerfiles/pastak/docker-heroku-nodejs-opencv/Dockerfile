# Inherit from Heroku's stack
FROM heroku/python

# Which version of node?
ENV NODE_ENGINE 4.1.1
# Locate our binaries
ENV PATH /app/heroku/node/bin/:/app/user/node_modules/.bin:$PATH

# Install OpenCV
RUN mkdir -p /app/.heroku/opencv /tmp/opencv
ADD Install-OpenCV /tmp/opencv
WORKDIR /tmp/opencv/Ubuntu
RUN echo 'deb http://archive.ubuntu.com/ubuntu trusty multiverse' >> /etc/apt/sources.list && apt-get update
RUN version=2.4.11 ./opencv_latest.sh

# Create some needed directories
RUN mkdir -p /app/heroku/node /app/.profile.d
WORKDIR /app/user

# Install node
RUN curl -s https://s3pository.heroku.com/node/v$NODE_ENGINE/node-v$NODE_ENGINE-linux-x64.tar.gz | tar --strip-components=1 -xz -C /app/heroku/node

# Export the node path in .profile.d
RUN echo "export PATH=\"/app/heroku/node/bin:/app/user/node_modules/.bin:\$PATH\"" > /app/.profile.d/nodejs.sh
RUN echo "export PKG_CONFIG_PATH=\"/app/.heroku/opencv/lib/pkgconfig\"" >> /app/.profile.d/nodejs.sh
RUN echo "export LD_LIBRARY_PATH=\"/app/.heroku/opencv/lib/:$LD_LIBRARY_PATH\"" >> /app/.profile.d/nodejs.sh

ONBUILD ADD package.json /app/user/
ONBUILD RUN /app/heroku/node/bin/npm install
ONBUILD ADD . /app/user/
