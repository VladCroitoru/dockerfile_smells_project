FROM    centos:centos6

# Enable EPEL for Node.js
RUN     rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm

# Install Node.js and npm
RUN     yum install -y npm

# Bundle app source
COPY . /src

# Install app dependencies
RUN cd /src; npm install

EXPOSE  8000
CMD ["node", "/src/index.js"]




### Cheat-sheet

## To build it:
## docker build -t myapp .

## To run it (note: needs to expose the port to the public):
## docker run -it -p 9000:8000 --rm --name webapp myapp

## To curl it:
## curl localhost:9000