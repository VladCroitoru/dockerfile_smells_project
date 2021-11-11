# deno not node because long-term deno will be used for all non-trivial scripting
FROM denoland/deno:alpine-1.13.1

RUN apk --no-cache --update add \
    bash \
    curl \
    git \
    jq \
    npm \
    openssh \
    ripgrep

# Needs edge repo
RUN apk add --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/testing \
    sd

# justfile for running commands, you will mostly interact with just https://github.com/casey/just
RUN VERSION=0.10.0 ; \
    SHA256SUM=661f3ebf1504f99cd96dfcb148f5e1d30e93c9c182680aab855cb881c3e0f13e ; \
    curl -L -O https://github.com/casey/just/releases/download/$VERSION/just-$VERSION-x86_64-unknown-linux-musl.tar.gz && \
    (echo "$SHA256SUM  just-$VERSION-x86_64-unknown-linux-musl.tar.gz" | sha256sum  -c) && \
    mkdir -p /tmp/just && mv just-$VERSION-x86_64-unknown-linux-musl.tar.gz /tmp/just && cd /tmp/just && \
    tar -xzf just-$VERSION-x86_64-unknown-linux-musl.tar.gz && \
    mkdir -p /usr/local/bin && mv /tmp/just/just /usr/local/bin/ && rm -rf /tmp/just
# just tweak: unify the just binary location on host and container platforms because otherwise the shebang doesn't work properly due to no string token parsing (it gets one giant string)
ENV PATH $PATH:/usr/local/bin
# alias "j" to just, it's just right there index finger
RUN printf '#!/bin/bash\njust "$@"' > /usr/bin/j && \
    chmod +x /usr/bin/j
ENV JUST_SUPPRESS_DOTENV_LOAD_WARNING=1

# watchexec for live reloading in development https://github.com/watchexec/watchexec
RUN VERSION=1.14.1 ; \
    SHA256SUM=34126cfe93c9c723fbba413ca68b3fd6189bd16bfda48ebaa9cab56e5529d825 ; \
    curl -L -O https://github.com/watchexec/watchexec/releases/download/$VERSION/watchexec-$VERSION-i686-unknown-linux-musl.tar.xz && \
    (echo "$SHA256SUM  watchexec-${VERSION}-i686-unknown-linux-musl.tar.xz" | sha256sum -c) && \
    tar xvf watchexec-$VERSION-i686-unknown-linux-musl.tar.xz watchexec-$VERSION-i686-unknown-linux-musl/watchexec -C /usr/bin/ --strip-components=1 && \
    rm -rf watchexec-*

# git on unconfigured systems requires these set for some operations
RUN git config --global user.email "ci@rob.ot"
RUN git config --global user.name "robot"

# Newer version of npm
RUN /usr/bin/npm i -g npm@7.21.1

# /repo is also hard-coded in the justfile
WORKDIR /repo
# Install cached modules
COPY package.json ./
COPY package-lock.json ./
RUN npm i

# Add user aliases to the shell if available
RUN echo "if [ -f /repo/.tmp/.aliases ]; then source /repo/.tmp/.aliases; fi" >> /root/.bashrc
