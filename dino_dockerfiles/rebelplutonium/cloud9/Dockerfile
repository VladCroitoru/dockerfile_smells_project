FROM fedora:28
RUN \
    dnf update --assumeyes && \
        dnf \
            install \
            --assumeyes \
            git \
            make \
            python \
            tar \
            which \
            bzip2 \
            ncurses \
            gmp-devel \
            mpfr-devel \
            libmpc-devel \
            glibc-devel \
            flex \
            bison \
            glibc-static \
            zlib-devel \
            gcc \
            gcc-c++ \
            nodejs \
            sudo \
            && \
            adduser user && \
            mkdir /opt/cloud9 && \
            mkdir /opt/cloud9/c9sdk && \
            git -C /opt/cloud9/c9sdk init && \
            git \
                -C /opt/cloud9/c9sdk \
                remote \
                add \
                origin \
                git://github.com/c9/core.git && \
            git -C /opt/cloud9/c9sdk pull origin master && \
            /opt/cloud9/c9sdk/scripts/install-sdk.sh && \
            sed \
                -i "s#127.0.0.1#0.0.0.0#g" \
                /opt/cloud9/c9sdk/configs/standalone.js && \
            sed \
                -i "s#opts[.]projectName = basename.opts[.]workspaceDir.;#opts.projectName = process.env.PROJECT_NAME#" \
                /opt/cloud9/c9sdk/plugins/c9.vfs.standalone/standalone.js && \
            curl \
                -L https://raw.githubusercontent.com/c9/install/master/install.sh | su -c "bash" user && \
            mkdir /opt/cloud9/bin && \
            mkdir /opt/cloud9/sbin && \
            mkdir /opt/cloud9/sudo && \
            mkdir /opt/cloud9/completion && \
            echo "#includedir /opt/cloud9/sudo" >> /etc/sudoers.d/cloud9 && \
            chmod 0444 /etc/sudoers.d/cloud9 && \
            echo "for FILE in \$(ls -1 /opt/cloud9/completion); do source /opt/cloud9/completion/\${FILE}; done" >> /home/user/.bashrc && \
            dnf update --assumeyes && \
            dnf clean all
COPY entrypoint.user.sh entrypoint.root.sh terminate.sh /opt/cloud9/scripts/
ENV CLOUD9_WORKSPACE=/opt/cloud9/workspace/workspace
ENTRYPOINT ["sh", "/opt/cloud9/scripts/entrypoint.root.sh"]
CMD []
ONBUILD COPY extension /opt/cloud9/extension
ONBUILD RUN \
    if [ -d /opt/cloud9/extension/sbin ]; then ls -1 /opt/cloud9/extension/sbin | while read FILE; do cp /opt/cloud9/extension/sbin/${FILE} /opt/cloud9/sbin/${FILE%.*} && chmod 0500 /opt/cloud9/sbin/${FILE%.*}; done; fi && \
        if [ -d /opt/cloud9/extension/bin ]; then ls -1 /opt/cloud9/extension/bin | while read FILE; do cp /opt/cloud9/extension/bin/${FILE} /opt/cloud9/bin/${FILE%.*} && chmod 0555 /opt/cloud9/bin/${FILE%.*}; done; fi && \
        if [ -d /opt/cloud9/extension/sudo ]; then ls -1 /opt/cloud9/extension/sudo | while read FILE; do cp /opt/cloud9/extension/bin/${FILE} /opt/cloud9/sudo/${FILE} && chmod 0444 /opt/cloud9/extension/bin/${FILE}; done; fi && \
        if [ -d /opt/cloud9/extension/completion ]; then ls -1 /opt/cloud9/extension/completion | while read FILE; do cp /opt/cloud9/extension/completion/${FILE} /opt/cloud9/completion/${FILE} && chmod 0444 /opt/cloud9/completion/${FILE}; done; fi && \
        if [ -f /opt/cloud9/extension/run.root.sh ]; then sh /opt/cloud9/extension/run.root.sh; fi && \
        if [ -f /opt/cloud9/extension/run.user.sh ]; then su -c "sh /opt/cloud9/extension/run.user.sh" user; fi
ONBUILD USER root