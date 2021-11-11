FROM dockerfile/python

RUN apt-get update
RUN apt-get install -y openssl

# From dockerfile/nodejs
# Compile Node.js
RUN \
  cd /tmp && \
  curl -L https://github.com/joyent/node/archive/v0.11.16.tar.gz | tar xzf - && \
  cd node-* && \
  ./configure && \
  CXX="g++ -Wno-unused-local-typedefs" make && \
  CXX="g++ -Wno-unused-local-typedefs" make install && \
  cd /tmp && \
  rm -rf /tmp/node-* && \
  echo '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bash_profile

ENV HOME /root

EXPOSE 80

RUN ln -s /usr/bin/nodejs /usr/bin/node

RUN mkdir -p /root/.ssh
ADD ssh_config /root/.ssh/config

ADD nodegear_bootstrap.sh /usr/local/bin/nodegear_bootstrap
RUN chmod +x /usr/local/bin/nodegear_bootstrap

CMD ["/usr/local/bin/nodegear_bootstrap"]
