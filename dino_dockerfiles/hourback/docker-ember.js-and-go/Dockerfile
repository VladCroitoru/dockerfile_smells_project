FROM hourback/docker-ember.js

RUN apt-get update

RUN apt-get install -yq wget mercurial ldap-utils

RUN wget https://storage.googleapis.com/golang/go1.5.2.linux-amd64.tar.gz

RUN tar -C /usr/local -xzf go1.5.2.linux-amd64.tar.gz

# Set up the development environment
RUN mkdir /gopath
RUN chown guest:guest /gopath
RUN echo "export GOPATH=/gopath" >> /home/guest/.profile

RUN echo 'export PATH=$PATH:/usr/local/go/bin' >> /home/guest/.profile

EXPOSE 8080
