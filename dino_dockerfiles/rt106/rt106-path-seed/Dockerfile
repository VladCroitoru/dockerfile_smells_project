# Copyright (c) General Electric Company, 2017.  All rights reserved.

FROM alpine:3.6

# update the image, add node and git (for bower)
RUN apk update && apk upgrade && apk add --update nodejs nodejs-npm && apk add git

# establish the user
# create non-privileged user and group
RUN addgroup -S rt106 && adduser -S -G rt106 rt106

# set up the folder structure
RUN mkdir /rt106
RUN chown rt106:rt106 /rt106

# install the custom code for the app (COPY does NOT set ownership based on USER?)
COPY . /rt106
RUN chown -R rt106:rt106 /rt106

# set the working directory
WORKDIR /rt106

# do everything else as this user
USER rt106:rt106

# install package dependencies
RUN npm install --production
# install all the browser level resources. do as one layer to keep image small: install the devDependencies and tools, install resources, remove devDependencies
RUN npm install --only=dev && ./node_modules/bower/bin/bower --allow-root install && npm prune --production

# configure the port
EXPOSE 8306

# entry point
CMD ["/rt106/entrypoint.sh"]
