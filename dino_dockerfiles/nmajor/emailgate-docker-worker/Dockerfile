FROM node:4.4.3-slim
# https://hub.docker.com/r/library/node/

RUN apt-get update
RUN apt-get install -y bzip2 libfontconfig pdftk pdfjam

# Download and install phantomjs
WORKDIR /tmp
RUN wget https://us-east.manta.joyent.com//nmajor/public/emailgate/container/phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN mv phantomjs-2.1.1-linux-x86_64/bin/phantomjs /bin/

# Copy pspdftool
COPY container/pspdftool /bin/

RUN apt-get install -y texlive-extra-utils
RUN apt-get install -y texlive-latex-recommended
RUN apt-get install -y poppler-utils
RUN apt-get install -y fonts-arphic-uming

# Copy over app source files
ENV HOME /var/app
RUN mkdir $HOME
WORKDIR $HOME
COPY package.json ./

RUN npm install
RUN npm install -g gulp

COPY . ./
RUN touch ./.env

RUN gulp babel

WORKDIR $HOME

CMD ["node", "dist/index.js", ">/tmp/stdout.log", "2>/tmp/stderr.log"]
