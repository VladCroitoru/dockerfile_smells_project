FROM debian:jessie


RUN apt-get update && apt-get install -y apt-utils&& apt-get install -y curl wget unzip \
    && apt-get install -y bzip2 build-essential chrpath libssl-dev libxft-dev \
# PhantomJS
    && apt-get install libfreetype6 libfreetype6-dev \
    && apt-get install libfontconfig1 libfontconfig1-dev \
    && cd ~ \
    && export PHANTOM_JS="phantomjs-1.9.8-linux-x86_64" \
    && wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2 \
    && tar xvjf $PHANTOM_JS.tar.bz2 \
    && mv $PHANTOM_JS /usr/local/share \
    && ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin \
# Install node
    && apt-get update \
    && apt-get install sudo \
    && curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - \
    && sudo apt-get install -y nodejs \
    && sudo npm install node-gyp -g \
# Install yarn
    && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list \
    && sudo apt-get update && sudo apt-get install yarn \
# Install jetty
    && curl -O http://repo1.maven.org/maven2/org/eclipse/jetty/jetty-distribution/9.3.12.v20160915/jetty-distribution-9.3.12.v20160915.tar.gz \
    && tar xzf jetty-distribution-9.3.12.v20160915.tar.gz \
    && mv jetty-distribution-9.3.12.v20160915 jettydir \ 
#Install java
    && echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list \
    && echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list \
    && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 \
    && apt-get update \
# Enable silent install
    && echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections \
    && echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections \
    && apt-get install -y oracle-java8-installer \
    && apt-get install oracle-java8-set-default \
# install maven
    && wget http://apache.mirrors.lucidnetworks.net/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz \
    && mkdir -p /usr/local/apache-maven \
    && mv apache-maven-3.3.9-bin.tar.gz /usr/local/apache-maven \
    && cd /usr/local/apache-maven && tar -xzvf apache-maven-3.3.9-bin.tar.gz \
# install browserstack local
    && wget https://www.browserstack.com/browserstack-local/BrowserStackLocal-linux-x64.zip \ 
    && unzip BrowserStackLocal-linux-x64.zip \
    && rm BrowserStackLocal-linux-x64.zip \
    && chmod +x BrowserStackLocal \
    && mv BrowserStackLocal /usr/local/bin



RUN echo 'export M2_HOME=/usr/local/apache-maven/apache-maven-3.3.9'  >> ~/.bashrc
RUN echo 'export M2=$M2_HOME/bin'  >> ~/.bashrc
RUN echo 'export MAVEN_OPTS="-Xms256m -Xmx512m"'  >> ~/.bashrc
RUN echo 'export PATH=$M2:$PATH'  >> ~/.bashrc