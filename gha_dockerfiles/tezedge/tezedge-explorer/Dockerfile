# base image
FROM node:16 AS BUILD_IMAGE

# set working directory
WORKDIR /app

# install angular cli
RUN npm install -g @angular/cli@12.2.2

# clone & install deps for repo
ARG branch=develop
ARG node_explorer_git="https://github.com/tezedge/tezedge-explorer"
RUN git clone ${node_explorer_git} && \
    cd tezedge-explorer && \
    git checkout ${branch} && \
    npm install && \
    node path.js

# change dir to angular app
WORKDIR /app/tezedge-explorer

# buid app
RUN ng build --configuration production --output-path=/dist

# remove development dependencies
RUN npm prune --production

################
# Run in NGINX #
################
FROM nginx:alpine
COPY --from=BUILD_IMAGE /dist /usr/share/nginx/html

ARG commit=local
ENV COMMIT=$commit

# When the container starts, replace the env.js with values from environment variables
CMD ["/bin/sh",  "-c",  "envsubst < /usr/share/nginx/html/assets/env.template.js > /usr/share/nginx/html/assets/env.js && exec nginx -g 'daemon off;'"]

# Example of how to run
# docker run --env SANDBOX='https://carthage.tezedge.com:3030' --env API='[{"id":"master","name":"master.dev.tezedge","http":"http://master.dev.tezedge.com:18733","monitoring":"http://master.dev.tezedge.com:38733/resources/tezedge","debugger":"http://master.dev.tezedge.com:17733","ws":false,"features":["MONITORING", "RESOURCES", "MEMPOOL_ACTION", "STORAGE_BLOCK", "NETWORK_ACTION", "LOGS_ACTION"],"resources":["system","storage","memory"]}]'  -p 8080:80  tezedge-explorer:latest
