FROM jnmik/docker-centos7-httpd-utilities-php5.6:latest
MAINTAINER Jean-Michael Cyr <cyrjeanmichael@gmail.com

# Install Node.js
RUN \
  cd /tmp && \
  wget http://nodejs.org/dist/node-latest.tar.gz && \
  tar xvzf node-latest.tar.gz && \
  rm -f node-latest.tar.gz && \
  cd node-v* && \
  ./configure && \
  CXX="g++ -Wno-unused-local-typedefs" make && \
  CXX="g++ -Wno-unused-local-typedefs" make install && \
  cd /tmp && \
  rm -rf /tmp/node-v* && \
  npm install -g npm@2.11.3 -g && \
  printf '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bashrc

# Documentation and References
# http://yomotherboard.com/how-to-install-upgrade-to-php-5-6-on-centos-rhel/
# http://devdocs.magento.com/guides/v2.0/install-gde/prereq/php-centos.html
# https://github.com/dockerfile/nodejs/blob/master/
# http://serverfault.com/questions/31393/installing-make-with-wget
# https://nodejs.org/download/release/
# http://dev.antoinesolutions.com/apache-server
# https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-a-centos-7-server