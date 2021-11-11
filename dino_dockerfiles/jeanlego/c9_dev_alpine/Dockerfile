FROM alpine:latest

ENV USR admin
ENV PAS letmein
ENV PRT 8080


# ------------------------------------------------------------------------------
# Switch to bash
RUN apk --update add bash tar
RUN sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd
RUN bash -i

# ------------------------------------------------------------------------------
# Install base
RUN apk --update add coreutils build-base g++ make curl wget openssl-dev apache2-utils git libxml2-dev sshfs nodejs bash tmux supervisor python python-dev py-pip \
 && rm -f /var/cache/apk/*

# ------------------------------------------------------------------------------
# Install Cloud9
RUN git clone https://github.com/c9/core.git /cloud9
RUN curl -s -L https://raw.githubusercontent.com/c9/install/master/link.sh | bash
RUN /cloud9/scripts/install-sdk.sh
RUN sed -i -e 's_127.0.0.1_0.0.0.0_g' /cloud9/configs/standalone.js

WORKDIR /root

# boot script
RUN echo "#!/bin/bash" > /startup.sh
RUN echo "cd /root" >> /startup.sh
RUN echo "[ ! -f /root/.bashrc ] && cp -af /root_bkp/. /root" >> /startup.sh
RUN echo "[ ! -d /root/tools ] && ln -s /STORAGE/tools /root/tools" >> /startup.sh
RUN echo "node /cloud9/server.js --listen 0.0.0.0 --port ${PRT} -w /root --collab -a ${USR}:${PAS} 2>&1 | tee .c9.log" >> /startup.sh
RUN chmod +x /startup.sh 

RUN curl -L https://github.com/rafi/etc-skel/archive/master.tar.gz | tar xzv --strip-components=1 --exclude README.md
RUN mkdir -p /root/.cache
RUN curl -o /root/.config/git/.git-prompt.sh https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh
RUN echo 'source /root/.config/git/.git-prompt.sh' >> /root/.bashrc


RUN echo "#!/bin/bash" > /install.sh
RUN echo "node /cloud9/server.js --listen 0.0.0.0 --port ${PRT} -w /root --collab -a ${USR}:${PAS} &" >> /install.sh
RUN echo "PROC=\$!" >> /install.sh
RUN echo "sleep 5" >> /install.sh
RUN echo "kill \${PROC}" >> /install.sh
RUN chmod +x /install.sh
RUN /bin/sh /install.sh

RUN cp -af /root /root_bkp
RUN mkdir /STORAGE

# expose port and directory
VOLUME /root
VOLUME /STORAGE

EXPOSE ${PRT}

ENTRYPOINT ["/bin/bash","/startup.sh"]
