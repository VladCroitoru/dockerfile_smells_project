FROM node:latest

RUN apt-get update

ARG USER="node"
ARG UID="1000"
ARG GID="1000"
ENV WORKSPACE="/blueprint/"

# set workspace.
RUN mkdir $WORKSPACE -p
WORKDIR $WORKSPACE

RUN npm config set unsafe-perm true

# install glup.
RUN npm init -y
RUN npm install gulp-cli -g
RUN npm install gulp -D
RUN npm install gulp-watch gulp-aglio gulp-plumber
RUN mkdir docs public
COPY gulpfile.js gulpfile.js

# support tools.
RUN apt-get install -y less vim

# set node user.
RUN groupmod -g $GID node && usermod -u $UID -g $GID $USER
RUN chown -R $UID:$GID $WORKSPACE
USER $USER

# command.
CMD gulp watch

