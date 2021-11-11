FROM node:8.11.4

LABEL maintainer="abner<contato@abner.io>"

RUN apt-get update && apt-get install --no-install-recommends -y sudo python gcc g++ make \
    && npm config set cache /cache/.npm/  \
    && sudo npm i -g npm --unsafe-perm \
    && sudo npm i -g node-sass@4.5.3 --unsafe-perm \
    && sudo npm i -g ionic@4.1.0 --unsafe-perm \
    && apt-get -y remove python gcc g++ make \
    && rm -rf /var/lib/apt/lists/*

RUN echo 'strict-ssl=false' > ~/.npmrc
RUN git config --global url."https://".insteadOf git://

