FROM node:14.16.0-alpine3.13 as builder
RUN apk add --update --no-cache \
    # Download some files
    curl \
    # compile some javascript native stuff (node-gyp)
    make gcc g++ python2 \
    # clone repositories (and also using ssh repositories)
    git openssh openssh-keygen mandoc git-doc \
    # Handle git diff properly
    less \
    # bash shell
    bash \
    # some lib to compile 'native-keymap' npm mpdule
    libx11-dev libxkbfile-dev \
    # requirements for keytar
    libsecret libsecret-dev

COPY code /vscode-compilation
WORKDIR /vscode-compilation
ENV ELECTRON_SKIP_BINARY_DOWNLOAD=1
RUN git init .
RUN yarn
RUN npm rebuild
RUN NODE_OPTIONS="--max_old_space_size=6500" ./node_modules/.bin/gulp checode-min
RUN cp -r ./out-assembly/checode-min /checode

RUN for f in "${HOME}" "/checode"; do\
           chgrp -R 0 ${f} && \
           chmod -R g+rwX ${f}; \
       done
RUN chmod a+x /checode/out/vs/che/node/entrypoint-loader.js

FROM quay.io/eclipse/che-machine-exec:next as machine-exec
FROM node:14.16.0-alpine3.13 as node-alpine-provider
FROM node:14.16.0-buster as node-buster-provider
FROM alpine:3.13.6

ENV HOME=/home/che
RUN apk add --update --no-cache \
    # Download some files
    curl \
    # clone repositories (and also using ssh repositories)
    git openssh openssh-keygen mandoc git-doc \
    # Handle git diff properly
    less \
    # bash shell
    bash \
    # some lib to compile 'native-keymap' npm mpdule
    libx11-dev libxkbfile-dev \
    libsecret \
    # nodejs lib
    libstdc++ \
    && adduser -D -S -u 1001 -G root -h /home/che -s /bin/sh che \
    && cat /etc/passwd | sed s#root:x.*#root:x:\${USER_ID}:\${GROUP_ID}::\${HOME}:/bin/bash#g > ${HOME}/passwd.template \
    && cat /etc/group | sed s#root:x:0:#root:x:0:0,\${USER_ID}:#g > ${HOME}/group.template
RUN mkdir /projects
RUN for f in "${HOME}" "/etc/passwd" "/etc/group" "/projects" ; do\
           chgrp -R 0 ${f} && \
           chmod -R g+rwX ${f}; \
       done

# copy node binary
COPY --from=node-alpine-provider /usr/local/bin/node /checode/bin/node-alpine
COPY --from=node-buster-provider /usr/local/bin/node /checode/bin/node-buster
COPY --from=builder /checode /checode
COPY --from=machine-exec /go/bin/che-machine-exec /checode/bin/machine-exec
COPY entrypoint.sh /entrypoint.sh
COPY entrypoint-init-container.sh /checode/entrypoint-init-container.sh
COPY entrypoint-volume.sh /checode/entrypoint-volume.sh
ENTRYPOINT /entrypoint.sh
WORKDIR /projects
USER che
