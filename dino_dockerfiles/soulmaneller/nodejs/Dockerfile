FROM ubuntu
MAINTAINER Oxoox Soulmaneller <oxoox22@gmail.com>

ENV ROOT_DIR /root
WORKDIR ${ROOT_DIR}

RUN /bin/bash -c 'apt-get update \
    && apt-get install curl git -y \
    && git clone https://github.com/creationix/nvm.git \
    && source /root/nvm/install.sh \
    && rm -rf /root/nvm \
    && source /root/.nvm/nvm.sh \
    && nvm install v6 \
    && nvm alias default 6'

RUN echo "{ \"allow_root\": true, \"interactive\": false }" >> ${ROOT_DIR}/.bowerrc
RUN echo "export NODE_PATH=$NODE_PATH:./lib:./" >> /root/.bashrc

CMD [ "/bin/bash" ]
