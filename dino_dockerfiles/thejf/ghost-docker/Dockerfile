FROM lopter/raring-base
MAINTAINER Jean-Francois Arseneau  <jf.arseneau@gmail.com>

# Update Ubuntu to the latest
RUN apt-get update
RUN apt-get upgrade -y

# Install latest Node.js
RUN apt-get install -y software-properties-common python g++ make
RUN add-apt-repository ppa:chris-lea/node.js
RUN apt-get update
RUN apt-get install -y nodejs

# Grab Ghost v0.3.2 and unpack
RUN apt-get install -y wget unzip
RUN wget https://ghost.org/zip/ghost-0.4.0.zip
RUN unzip -uo ghost-0.4.zip

# Install Ghost dependencies
RUN npm install --production

# Set up config
RUN apt-get install -y git
RUN git clone https://gist.github.com/6979674.git
RUN cp 6979674/config.js config.js

EXPOSE 2368
