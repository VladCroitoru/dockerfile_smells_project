FROM codetroopers/jenkins-slave-jdk8-android:22-22.0.1-x86

MAINTAINER Shashikant Jagtap shashikant.jagtap@aol.co.uk

RUN apt-get update
RUN apt-get -y install curl build-essential

RUN apt-get install -y nginx openssh-server git-core openssh-client curl
RUN apt-get install -y nano
RUN apt-get install -y build-essential
RUN apt-get install -y openssl libreadline6 libreadline6-dev curl zlib1g zlib1g-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt-dev autoconf libc6-dev ncurses-dev automake libtool bison subversion pkg-config

# install RVM, Ruby, and Bundler
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
RUN \curl -L https://get.rvm.io | bash -s stable
RUN /bin/bash -l -c "rvm requirements"
RUN /bin/bash -l -c "rvm install 2.0"
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"
RUN /bin/bash -l -c "gem install bddfire -v 1.9.7 --no-ri --no-rdoc"
RUN /bin/bash -l -c "gem install cucumber --no-ri --no-rdoc"
RUN /bin/bash -l -c "gem install capybara --no-ri --no-rdoc"
RUN /bin/bash -l -c "gem install poltergeist --no-ri --no-rdoc"
RUN /bin/bash -l -c "gem install rspec --no-ri --no-rdoc"
RUN /bin/bash -l -c "gem install appium_lib --no-ri --no-rdoc"
RUN /bin/bash -l -c "bddfire fire_cucumber"
RUN /bin/bash -l -c "cd cucumber&&bundle install"

#Install maven
RUN apt-get install -y maven

USER jenkins
WORKDIR /home/jenkins

RUN  mkdir .local && mkdir node
RUN curl http://nodejs.org/dist/node-latest.tar.gz | tar xz --strip-components=1
RUN ./configure --prefix=.local && make install

ENV NODE_PATH=/home/jenkins/.local/lib/node_modules
ENV PATH=/home/jenkins/.local/bin:$PATH


USER root
# Expose bin to default nodejs bin for sublime plugins
RUN ln -s /home/jenkins/.local/bin/node  /usr/bin/nodejs
RUN ln -s /home/jenkins/.local/lib/node_modules /usr/local/lib/

ENV appium_args "-p 4723"

USER jenkins
#Install npm
RUN curl -O https://npmjs.com/install.sh | sh

ENV appium_version 1.4.10
#Install appium
RUN npm install -g appium@${appium_version}

ENV phantomjs_version 1.9.7
#Install PhantomJS
RUN npm install -g phantomjs

ADD files/insecure_shared_adbkey /home/jenkins/.android/adbkey
ADD files/insecure_shared_adbkey.pub /home/jenkins/.android/adbkey.pub

USER root
RUN apt-get -y install supervisor
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN adb kill-server
RUN adb start-server
RUN adb devices
EXPOSE 22
CMD ["/usr/bin/supervisord"]
