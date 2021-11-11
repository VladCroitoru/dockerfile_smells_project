# Atom Docker Image For Package Testing
FROM ubuntu:trusty
MAINTAINER Lukas Eipert <leipert@users.noreply.github.com>

ADD ./dpkg-dep.sh .

ENV atomDownloadLink \
https://github.com/atom/atom/releases/download/v1.3.1/atom-amd64.deb

ENV atomDownloadName \
atom-amd64.deb

ENV atomBuildDependencies curl

ENV atomDependencies\
 ca-certificates\
 make g++\
 xvfb libasound2

RUN \
    # Make Sure We're Up To Date
    DEBIAN_FRONTEND=noninteractive \
    apt-get update -yqq \
 && DEBIAN_FRONTEND=noninteractive \
    apt-get dist-upgrade -fyqq > /dev/null \
    # Install dependencies
 && DEBIAN_FRONTEND=noninteractive \
    apt-get install -fyqq \
    ${atomBuildDependencies}\
    ${atomDependencies}\
    --no-install-recommends > /dev/null \
    # Download and install atom in the version specified
 && curl -sL -o ${atomDownloadName} ${atomDownloadLink} \
 && bash ./dpkg-dep.sh ${atomDownloadName} \
 && rm -rf ${atomDownloadName} \
    # Cleanup
 && DEBIAN_FRONTEND=noninteractive \
    apt-get purge -yqq ${atomBuildDependencies} \
 && DEBIAN_FRONTEND=noninteractive \
    apt-get autoremove -yqq \
 && DEBIAN_FRONTEND=noninteractive \
    apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    # Test if apm works
 && apm --version


RUN \
    # Symlink node, npm to atoms node & npm.
    ln -s /usr/share/atom/resources/app/apm/bin/node /usr/local/share/node \
 && ln -s /usr/share/atom/resources/app/apm/bin/node /usr/local/bin/node \
 && ln -s /usr/share/atom/resources/app/apm/bin/node /usr/bin/node \
 && ln -s /usr/share/atom/resources/app/apm/node_modules/.bin/npm \
    /usr/local/share/npm \
 && ln -s /usr/share/atom/resources/app/apm/node_modules/.bin/npm \
    /usr/local/bin/npm \
 && ln -s /usr/share/atom/resources/app/apm/node_modules/.bin/npm /usr/bin/npm \
    # Install grunt and gulp.
 && npm i -g gulp grunt-cli > /dev/null \
 && npm cache clean \
    # Test if node, npm, gulp && grunt works
 && node --version && npm --version  && gulp --version && grunt --version

CMD \
    echo "`git --version`"\
 && echo "node version: `node --version`"\
 && echo "npm version: `npm --version`"\
 && echo "gulp version: `gulp --version`"\
 && echo "grunt version:  `grunt --version`"\
 && echo "apm version:  `apm --version`"
