## BUILDING
##   (from project root directory)
##   $ docker build -t node-js-for-kmaster360-deezloader .
##
## RUNNING
##   $ docker run -p 3000:3000 node-js-for-kmaster360-deezloader
##
## CONNECTING
##   Lookup the IP of your active docker host using:
##     $ docker-machine ip $(docker-machine active)
##   Connect to the container at DOCKER_IP:3000
##     replacing DOCKER_IP for the IP of your active docker host

FROM gcr.io/bitnami-containers/minideb-extras:jessie-r13-buildpack

MAINTAINER Bitnami <containers@bitnami.com>

ENV STACKSMITH_STACK_ID="5vxz7hu" \
    STACKSMITH_STACK_NAME="Node.js for kmaster360/Deezloader" \
    STACKSMITH_STACK_PRIVATE="1"

RUN bitnami-pkg install node-6.3.1-0 --checksum afc84696d6aeaf8a3d058ecda07f72bfa54392207fa939e6b11ef8eba986aff9

ENV PATH=/opt/bitnami/node/bin:/opt/bitnami/python/bin:$PATH \
    NODE_PATH=/opt/bitnami/node/lib/node_modules

## STACKSMITH-END: Modifications below this line will be unchanged when regenerating

# ExpressJS template
COPY . /app
WORKDIR /app

RUN npm install

EXPOSE 3000
CMD ["node", "app.js"]
