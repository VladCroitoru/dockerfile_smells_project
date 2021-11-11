###############################################################################
# NodeJS                                                                      #
#                                                                             #
# Version 0.1, Copyright (C) 2017 Gregory D. Horne                            #
#                                                                             #
# Licensed under the terms of the 3-Clause BSD License                        #
###############################################################################


# create the container image
# docker build -t nodejs .

# instantiate a transient instance of the container
#  (out-of-container storage)
# docker run -i -t -v ${PWD}:/opt/project --rm nodejs [[node ... | npm ...]]

# instantiate a persistent instance of the container 
# (optional out-of-container storage)
# docker run -i -t [-v ${PWD}:/opt/project] --name nodejs [[node ... | npm ...]] 
# start the container instance
# docker start nodejs
# use the container instance (interactive mode for node with `-i -t`)
# docker exec [-i -t] nodejs [node ... | npm ...]
# stop the container instance
# docker stop nodejs
# delete the container instance (in-container storage will be deleted too!)
# docker stop nodejs && docker rm nodejs

FROM alpine:3.7

MAINTAINER Gregory D. Horne <greg at gregoryhorne dot ca>

# Create non-privileged user account and a gemeric mount point

RUN \
    mkdir -p /opt/project \
    && adduser -D nodejs \
    && chown -R nodejs:nodejs /opt/project

# install nodejs and npm

RUN \
    apk --no-cache update upgrade \
    && apk --no-cache add nodejs nodejs-npm

# set run-time environment

USER nodejs
VOLUME /opt/project
WORKDIR /opt/project

CMD ["/usr/bin/node"]
