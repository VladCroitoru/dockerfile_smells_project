# try to make this more efficient
FROM debian:bullseye-slim AS build-tools

RUN \
  echo "# INSTALL BUILD DEPENDENCIES ##########################################" && \
  apt-get update && \
  apt upgrade -y && apt dist-upgrade && \
  apt-get install -y build-essential "linux-headers-*-common" libcurl4-gnutls-dev curl g++ gcc git make nodejs npm python3 python3-distutils vim && \
  mkdir -p /tmp

RUN \
  echo "# FETCH INSTALLATION FILES ######################################" && \
  cd /tmp && \
  git clone --recursive --progress https://github.com/briancullinan/planet_quake && \
  cd /tmp/planet_quake && \
  git submodule add -f git://github.com/emscripten-core/emsdk.git libs/emsdk && \
  git submodule update --init --recursive --progress

# update the copy from cache to latest from github
FROM build-tools AS build-latest

# TODO: checkout different branches for different experimental features
RUN \
  echo "# UPDATE SOURCE FILES ######################################" && \
  cd /tmp/planet_quake && \
  git status && \
  git pull && \
  cd /tmp/planet_quake/libs/emsdk && \
  git pull

FROM build-latest AS build-ded

RUN \
  echo "# BUILD NATIVE SERVER ##########################################" && \
  cd /tmp/planet_quake && \
  make clean release BUILD_CLIENT=0 NOFPU=1

FROM build-latest AS build-js

RUN \
  echo "# INSTALL NODE AND EMSDK ######################################" && \
  cd /tmp/planet_quake && \
  echo "" > /tmp/planet_quake/libs/emsdk/upstream/emscripten/.emscripten && \
  echo "BINARYEN_ROOT = '/tmp/planet_quake/libs/emsdk/upstream'" >> /tmp/planet_quake/libs/emsdk/upstream/emscripten/.emscripten && \
  echo "LLVM_ROOT = '/tmp/planet_quake/libs/emsdk/upstream/bin'" >> /tmp/planet_quake/libs/emsdk/upstream/emscripten/.emscripten && \
  echo "NODE_JS = '/usr/bin/node'" >> /tmp/planet_quake/libs/emsdk/upstream/emscripten/.emscripten && \
  echo "EM_CACHE = '/tmp/planet_quake/libs/emsdk/upstream/emscripten/cache'" >> /tmp/planet_quake/libs/emsdk/upstream/emscripten/.emscripten && \
  npm install && \
  npm run install:emsdk && \
  mkdir -p /tmp/planet_quake/libs/emsdk/upstream/emscripten/cache && \
  export EM_CACHE=/tmp/planet_quake/libs/emsdk/upstream/emscripten/cache && \
  export EMSCRIPTEN_CACHE=/tmp/planet_quake/libs/emsdk/upstream/emscripten/cache && \
  npm run install:libs

RUN \
  echo "# BUILD JS CLIENT ##########################################" && \
  cd /tmp/planet_quake && \
  export STANDALONE=1 && \
  make clean release EMSCRIPTEN_CACHE=/tmp/planet_quake/libs/emsdk/upstream/emscripten/cache PLATFORM=js

FROM node:15.12-slim as serve-tools

RUN \
  echo "# INSTALL CONTENT DEPENDENCIES #################################" && \
  apt-get update && \
  apt-get install -y git && \
  mkdir -p /home/baseq3 && \
  mkdir -p /tmp

RUN \
  echo "# FETCH RUN FILES #################################" && \
  cd /tmp && \
  git clone --progress https://github.com/briancullinan/planet_quake

FROM node:15.12-slim AS serve-content

RUN mkdir -p /tmp/planet_quake/code/wasm/bin
RUN mkdir -p /tmp/planet_quake/code/wasm/lib
RUN mkdir -p /tmp/planet_quake/build/release-js-js
RUN mkdir -p /tmp/planet_quake/build/release-linux-x86_64

COPY --from=serve-tools /tmp/planet_quake/package.json /tmp/planet_quake/package.json
COPY --from=serve-tools /tmp/planet_quake/code/wasm/bin /tmp/planet_quake/code/wasm/bin
COPY --from=serve-tools /tmp/planet_quake/code/wasm/lib /tmp/planet_quake/code/wasm/lib
COPY --from=build-js /tmp/planet_quake/build/release-js-js/quake3e* /tmp/planet_quake/build/release-js-js/
COPY --from=build-ded /tmp/planet_quake/build/release-linux-x86_64/quake3e* /tmp/planet_quake/build/release-linux-x86_64/

RUN \
  cd /tmp/planet_quake && \
  npm install --dev

EXPOSE 8080/tcp
EXPOSE 27960/udp
VOLUME [ "/home/baseq3" ]
ENV RCON=password123!
ENV GAME=baseq3-cc
ENV BASEGAME=baseq3-cc

CMD node /tmp/planet_quake/code/wasm/bin/web.js --temp /home

FROM serve-content AS serve-quake3e

CMD /tmp/planet_quake/build/release-linux-x86_64/quake3e.ded.x64 \
  +cvar_restart +set net_port 27960 +set fs_basepath /home \
  +set dedicated 2 +set fs_homepath /home \
  +set fs_basegame ${BASEGAME} +set fs_game ${GAME} \
  +set ttycon 0 +set rconpassword ${RCON} \
  +set logfile 2 +set com_hunkmegs 150 +set vm_rtChecks 0 \
  +set sv_maxclients 32 +set sv_pure 0 +exec server.cfg

FROM serve-content AS serve-both

CMD \
  (node /tmp/planet_quake/code/wasm/bin/web.js --temp /home &) && \
  /tmp/planet_quake/build/release-linux-x86_64/quake3e.ded.x64 \
    +cvar_restart +set net_port 27960 +set fs_basepath /home \
    +set dedicated 2 +set fs_homepath /home \
    +set fs_basegame ${BASEGAME} +set fs_game ${GAME} \
    +set ttycon 0 +set rconpassword ${RCON} \
    +set logfile 2 +set com_hunkmegs 150 +set vm_rtChecks 0 \
    +set sv_maxclients 32 +set sv_pure 0 +exec server.cfg

FROM serve-tools AS repack

RUN \
  echo "# INSTALL REPACK DEPENDENCIES ##########################################" && \
  apt-get update && \
  apt-get install -y systemd imagemagick imagemagick-common vorbis-tools vim python && \
  cd /tmp/planet_quake && \
  npm install --dev

VOLUME [ "/home/baseq3" ]

CMD node /tmp/planet_quake/code/wasm/bin/repack.js --no-graph --no-overwrite --temp /home /home/baseq3

########### TODO REPACK DOCKER HERE ############
# needs a data source for baseq3 content, Github with demo data maybe?

FROM serve-both AS full

COPY --from=briancullinan/quake3e:baseq3 /home/baseq3-cc /home/baseq3-cc

FROM quay.io/parkervcp/pterodactyl-images:debian_nodejs-14 AS serve-pterodactyl

RUN mkdir -p /tmp/planet_quake/code/wasm/bin
RUN mkdir -p /tmp/planet_quake/code/wasm/lib
RUN mkdir -p /tmp/planet_quake/build/release-js-js
RUN mkdir -p /tmp/planet_quake/build/release-linux-x86_64

COPY --from=briancullinan/quake3e:serve-tools /tmp/planet_quake/package.json /tmp/planet_quake/package.json
COPY --from=briancullinan/quake3e:serve-tools /tmp/planet_quake/code/wasm/bin /tmp/planet_quake/code/wasm/bin
COPY --from=briancullinan/quake3e:serve-tools /tmp/planet_quake/code/wasm/lib /tmp/planet_quake/code/wasm/lib
COPY --from=briancullinan/quake3e:build-js /tmp/planet_quake/build/release-js-js/quake3e* /tmp/planet_quake/build/release-js-js/
COPY --from=briancullinan/quake3e:build-ded /tmp/planet_quake/build/release-linux-x86_64/quake3e* /tmp/planet_quake/build/release-linux-x86_64/
COPY --from=briancullinan/quake3e:baseq3 /home/baseq3-cc /home/baseq3-cc

# Run latest dockerhub image:
# docker run -ti -p 8080:8080 -p 27960:27960/udp briancullinan/quake3e:full
# Build an image to repack
# docker build --target repack
# Run repack image
# docker run -ti -v /Applications/ioquake3/baseq3:/home/baseq3 --name quake3e briancullinan/quake3e:repack
