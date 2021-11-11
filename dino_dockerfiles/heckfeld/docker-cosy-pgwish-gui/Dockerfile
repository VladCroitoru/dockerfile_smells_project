# Start COSY QBL GUI
#
FROM heckfeld/docker-cosy-pgwish

EXPOSE 22
EXPOSE 8444

RUN apt-get update && \
    apt-get install -y openssl ssh x11-apps && \
    rm -rf /var/lib/apt/lists/*
RUN mkdir -p /var/run/sshd
RUN update-rc.d ssh disable
RUN delgroup operator && \
    useradd -c "COSY Operator" \
            -d /home/operator -m \
            -s /bin/bash \
            -u 160 -g users operator

RUN mkdir -p /home/operator/.ssh
COPY id_rsa.pub /home/operator/.ssh/authorized_keys
RUN chown -R operator:users /home/operator
RUN chmod og-w /home/operator/.ssh/authorized_keys
ENTRYPOINT [ "/usr/sbin/sshd", "-D", "-f","/etc/ssh/sshd_config", "-E", "/tmp/sshd.log", "-4" ]
