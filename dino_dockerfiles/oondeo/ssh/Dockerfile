FROM oondeo/alpine

# Step 1: sshd needs /var/run/sshd/ to run
# Step 2: Remove keys, they will be generated later by entrypoint
#         (unique keys for each container)
RUN apk-install openssh-sftp-server openssh bash rsync p7zip unrar lzip bzip2 gzip tar && \
    chmod 700 /usr/bin/ssh && \
    mkdir -p /var/run/sshd && \
    rm -f /etc/ssh/ssh_host_*key*

VOLUME /etc/ssh

EXPOSE 22

ENV SSH="no"
ADD entrypoint /usr/local/sbin/entrypoint
ADD sshconfig /usr/local/sbin/sshconfig

ENTRYPOINT ["/usr/local/sbin/entrypoint"]


