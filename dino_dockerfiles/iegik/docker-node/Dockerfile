FROM tatsushid/tinycore:6.4-x86
ENV CORE x86 
ENV NODE_VERSION 8.9.4
ENV NPM_VERSION 5.8.0

RUN tce-load -wic gnupg curl \
    && rm -rf /tmp/tce/optional/*

RUN tce-load -wic coreutils \
        binutils \
        git \
        openssh \
        file \
    && cd /tmp \
    && curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v${NODE_VERSION}-linux-${CORE}.tar.gz" \
    && curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
    && grep " node-v${NODE_VERSION}-linux-${CORE}.tar.gz" SHASUMS256.txt.asc | sha256sum -c - \
    && tar -xzf "node-v${NODE_VERSION}-linux-${CORE}.tar.gz" \
    && rm -f "node-v${NODE_VERSION}-linux-${CORE}.tar.gz" SHASUMS256.txt.asc \
    && cd "/tmp/node-v${NODE_VERSION}-linux-${CORE}" \
    && for F in `find . | xargs file | grep "executable" | grep ELF | grep "not stripped" | cut -f 1 -d :`; do \
            [ -f $F ] && strip --strip-unneeded $F; \
        done \
    && sudo cp -R . /usr/local \
    && cd / \
    && sudo ln -s /lib /lib64 \
    && rm -rf "/tmp/node-v${NODE_VERSION}-linux-${CORE}" \
    && cd /tmp/tce/optional \
    && for PKG in acl.tcz \
                libcap.tcz \
                coreutils.tcz \
                binutils.tcz \
                file.tcz; do \
            echo "Removing $PKG files"; \
            for F in `unsquashfs -l $PKG | grep squashfs-root | sed -e 's/squashfs-root//'`; do \
                [ -f $F -o -L $F ] && sudo rm -f $F; \
            done; \
            INSTALLED=$(echo -n $PKG | sed -e s/.tcz//); \
            sudo rm -f /usr/local/tce.installed/$INSTALLED; \
        done \
    && rm -rf /tmp/tce/optional/* \
    && sudo npm install -g npm@"$NPM_VERSION"
WORKDIR /root
USER root
