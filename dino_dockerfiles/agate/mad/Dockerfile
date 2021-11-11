FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y build-essential libssl-dev curl git

RUN curl -sL https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | NVM_DIR=/usr/local/nvm bash

RUN curl -sL https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 > /usr/local/bin/dumb-init 
RUN chmod +x /usr/local/bin/dumb-init

ENV TMP_MAD_PATH /tmp/mad
RUN mkdir $TMP_MAD_PATH

ADD .nvmrc $TMP_MAD_PATH
RUN bash -c "source /usr/local/nvm/nvm.sh && cd $TMP_MAD_PATH && nvm install"

ADD package-lock.json $TMP_MAD_PATH
ADD package.json $TMP_MAD_PATH
RUN bash -c "source /usr/local/nvm/nvm.sh && cd $TMP_MAD_PATH && npm install"

ADD docker.launch.sh /usr/local/bin

ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]
CMD ["docker.launch.sh"]
