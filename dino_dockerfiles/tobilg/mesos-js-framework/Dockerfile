FROM java:openjdk-8-jdk

# Overall ENV vars
ENV APP_BASE_PATH /app
ENV MESOS_VERSION 0.27.2-2.0.15.debian81
ENV NODE_VERSION v5.8.0

# Add package sources and install
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \
    echo "deb http://repos.mesosphere.io/debian jessie main" | tee /etc/apt/sources.list.d/mesosphere.list && \
    echo "deb http://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list && \
    apt-get update && \
    apt-get install --no-install-recommends -y --force-yes mesos=$MESOS_VERSION \
    wget \
    python \
    make \
    gcc \
    build-essential \
    g++

# Install Node.js 5.x
RUN wget --no-check-certificate https://nodejs.org/dist/$NODE_VERSION/node-$NODE_VERSION-linux-x64.tar.gz && \
    tar -C /usr/local --strip-components 1 -xzf node-$NODE_VERSION-linux-x64.tar.gz && \
    rm node-$NODE_VERSION-linux-x64.tar.gz

# Add mesos-js-framework files
ADD mesos-js-framework.js $APP_BASE_PATH/
ADD package.json $APP_BASE_PATH/
ADD ./lib $APP_BASE_PATH/lib
ADD ./libs $APP_BASE_PATH/libs

# Setup of the mesos-js-framework
RUN cd $APP_BASE_PATH && \
    chmod +x mesos-js-framework.js && \
    npm install -g node-gyp && \
    npm install

CMD ["node", "/app/mesos-js-framework.js"]