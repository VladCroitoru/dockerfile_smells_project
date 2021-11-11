################################################################################
#                                                                              #
#                                 {o,o}                                        #
#                                 |)__)                                        #
#                                 -"-"-                                        #
#                                                                              #
################################################################################
#
#
#
#################################---FROM---#####################################

FROM ubuntu

################################################################################

#################################---INFO---#####################################

MAINTAINER Lovrenc Avsenek <a.lovrenc@gmail.com>

################################################################################

#################################---ENV---######################################

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN=true

################################################################################

################################---BUILD---#####################################

RUN apt-get update; \
    echo "tzdata tzdata/Areas select Europe \
tzdata tzdata/Zones/Europe select Ljubljana" > /opt/tzdefault; \
    debconf-set-selections /opt/tzdefault; \
    apt-get upgrade --yes; \
    apt-get install --yes \
        curl \
        git \
        npm && \
    apt-get clean

RUN curl -sL https://deb.nodesource.com/setup_15.x | bash - ;\
    apt-get install -y -q \
        nodejs; \
    npm install -g npm
RUN npm install --global \
        gulpjs/gulp-cli \
        webpack \
        webpack-cli

################################################################################
