FROM alpine

MAINTAINER Henrik Jonsson <me@hkjn.me>

RUN apk add --no-cache python g++ && \
    adduser brave -D && \
    apk add --no-cache make git nodejs python && \
    chown brave:brave /usr/lib/node_modules
# TODO(hkjn): Understand why the bloom-filter-cpp package needs to be installed as nonprivileged user.
USER brave
RUN npm install -g bloom-filter-cpp
USER root

RUN npm install -g node-gyp@3.2.1 && \
    apk add --no-cache xvfb libgnome-keyring-dev
RUN npm install -g mocha babel-register electron
USER brave
WORKDIR /home/brave/
RUN mkdir -p src/github.com/brave && \
    cd src/github.com/brave && \
    git clone https://github.com/brave/browser-laptop
WORKDIR /home/brave/src/github.com/brave/browser-laptop

# TODO(hkjn): Reenable tests if they can be fixed:
# browser-laptop/test/lib/urlutilTest.js:10
#    it('null for empty', regeneratorRuntime.mark(function _callee() {
#		                         ^
# ReferenceError: regeneratorRuntime is not defined
# RUN npm test

# TODO(hkjn): Find why binding.gyp isn't found / what if anything breaks due to this:
# gyp: binding.gyp not found (cwd: /home/brave/src/github.com/brave/browser-laptop/node_modules/lru_cache) while trying to load binding.gyp
RUN npm install
RUN npm run lint
# TODO(hkjn): Re-enable building abp-filter-parser-cpp, if it is
# indeed necessary. If so we need to find why "npm install" looks for
# node-gyp in the wrong place:
# /bin/sh: ./node_modules/.bin/node-gyp: not found
# The equivalent node-gyp command in the "npm install" command above
# seems to work fine, as this line is logged:
# https://github.com/brave/browser-laptop/blob/master/tools/rebuildNativeModules.js#L4
# Seems that rebuilding native modules can be done separately:
# node ./tools/rebuildNativeModules.js
# WORKDIR /home/brave/src/github.com/brave/browser-laptop/node_modules/abp-filter-parser-cpp
# RUN make

CMD ["npm", "start"]