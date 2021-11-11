FROM ubuntu
ENV DEBIAN_FRONTEND = noninteractive

WORKDIR /usr/src/app

RUN apt update 
RUN apt -y install build-essential
RUN apt -y install curl 
ENV NVM_DIR /root/.nvm
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash \
    && . $NVM_DIR/nvm.sh 
# RUN $NVM_DIR/nvm
# && nvm alias default $NODE_VERSION \
# && nvm use default
# RUN export NVM_DIR="$HOME/.nvm"
RUN [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
RUN [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
# RUN nvm --version
# RUN nvm install node 
# # RUN apt -y install nodejs npm
# RUN node -v
# RUN npm -v
# # RUN apk update && apk add --update alpine-sdk
# # RUN apk add --update --no-cache python3
# # RUN apk add --no-cache --upgrade bash
# RUN npm install --global yarn
# COPY package*.json ./
# RUN yarn install
# COPY ./build/main .

# EXPOSE 8080

# CMD [ "node", "run.js" ]