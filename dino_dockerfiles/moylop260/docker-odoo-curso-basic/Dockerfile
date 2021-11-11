FROM ubuntu:16.04
ADD install.sh /install.sh
RUN /install.sh myosusr && \
        rm -rf /tmp/* && \
        find /var/tmp -type f -print0 | xargs -0r rm -rf && \
        find /var/log -type f -print0 | xargs -0r rm -rf && \
        find /var/lib/apt/lists -type f -print0 | xargs -0r rm -rf && \
        echo 'myosusr ALL=NOPASSWD: ALL' >> /etc/sudoers

USER myosusr
WORKDIR /home/myosusr
RUN git --git-dir=/home/myosusr/odoo-repo/.git gc --aggressive && \
        git --git-dir=/home/myosusr/odoo-repo/.git fetch origin 10.0 --depth=10
