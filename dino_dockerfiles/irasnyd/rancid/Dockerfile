FROM centos:7

# install supercronic
ENV SUPERCRONIC_URL=https://github.com/aptible/supercronic/releases/download/v0.1.8/supercronic-linux-amd64 \
    SUPERCRONIC=supercronic-linux-amd64 \
    SUPERCRONIC_SHA1SUM=be43e64c45acd6ec4fce5831e03759c89676a0ea

RUN curl -fsSLO "$SUPERCRONIC_URL" \
 && echo "${SUPERCRONIC_SHA1SUM}  ${SUPERCRONIC}" | sha1sum -c - \
 && chmod +x "$SUPERCRONIC" \
 && mv "$SUPERCRONIC" "/usr/bin/${SUPERCRONIC}" \
 && ln -s "/usr/bin/${SUPERCRONIC}" /usr/bin/supercronic

ENV RANCID_VERSION 3.10

# install build-time and run-time dependencies
RUN yum -y install epel-release \
        && yum -y install bash curl cvs expect gcc git make openssh-clients perl ssmtp subversion telnet \
        && yum -y clean all

# install rancid
# patch for explicit email user (remove aliases support)
# patch for logs to stdout/stderr
RUN curl -O ftp://ftp.shrubbery.net/pub/rancid/rancid-${RANCID_VERSION}.tar.gz \
        && tar xzf rancid-${RANCID_VERSION}.tar.gz \
        && pushd rancid-${RANCID_VERSION} \
        && sed -i -e 's@ - courtesy of $mailrcpt@@' bin/control_rancid.in \
        && sed -i -e 's@>$LOGDIR/$GROUP.*$@@' bin/rancid-run.in \
        && ./configure --prefix=/usr --sysconfdir=/etc/rancid --localstatedir=/var/rancid \
        && make \
        && make install \
        && popd \
        && rm -rf rancid-${RANCID_VERSION} rancid-${RANCID_VERSION}.tar.gz \
        && groupadd -g 1000 rancid \
        && useradd -m -u 1000 -g 1000 -s /bin/bash -d /var/rancid -c RANCID rancid \
        && chown -R rancid:rancid /var/rancid \
        && mkdir -p /var/log/rancid \
        && chown -R rancid:rancid /var/log/rancid

# symlink rancid configuration file to use repository version
RUN rm -f /etc/rancid/rancid.conf \
        && ln -s /var/rancid/rancid.conf /etc/rancid/rancid.conf

# symlink ssmtp configuration file to use repository version
RUN rm -f /etc/ssmtp/ssmtp.conf \
        && ln -s /var/rancid/ssmtp.conf /etc/ssmtp/ssmtp.conf

# wrap ssh to avoid strict host key checking
RUN mv /usr/bin/ssh /usr/bin/ssh.orig
COPY ssh-wrapper /usr/bin/ssh

# set up entrypoint
COPY docker-entrypoint.sh /
ENTRYPOINT [ "/docker-entrypoint.sh" ]
CMD [ "/bin/bash" ]

# use an unprivileged user account
WORKDIR /var/rancid
USER rancid
