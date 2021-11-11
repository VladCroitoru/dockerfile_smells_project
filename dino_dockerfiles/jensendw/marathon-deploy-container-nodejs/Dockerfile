FROM jensendw/marathon-deploy-container:1.1

RUN echo "http://dl-cdn.alpinelinux.org/alpine/v3.7/main" >> /etc/apk/repositories

RUN apk update && apk add openssl && apk add nodejs

# https://github.com/facebook/flow/issues/3649
RUN wget -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.25-r0/glibc-2.25-r0.apk
RUN apk add glibc-2.25-r0.apk

RUN npm install -g yarn
