FROM debian:jessie

MAINTAINER Milo Casagrande <milo.casagrande@linaro.org>
LABEL Version="1.0" Description="Run gitolite in a container"

RUN apt-get clean && apt-get update && apt-get install -y -qq \
    sudo \
    openssh-server \
    git \
    git-core \
    python3 \
    python3-redis \
    python3-zmq \
    python3-requests

# The git user.
RUN adduser --system --group --shell /bin/sh git

RUN su git -c "mkdir /home/git/bin"
RUN cd /home/git; su git -c "git clone git://github.com/sitaramc/gitolite";
RUN cd /home/git/gitolite; su git -c "git checkout v3.6.5 &>/dev/null";
RUN cd /home/git; gitolite/install -ln /usr/local/bin
COPY gitolite.rc /home/git/.gitolite.rc

RUN cd /home/git; su git -c "git clone https://github.com/linaro-product/gitci-key-signup.git key-signup"

# https://github.com/docker/docker/issues/5892
RUN chown -R git:git /home/git

# Missing privilege separation directory: /var/run/sshd
RUN mkdir /var/run/sshd

# Copy the sshd config at the right place.
COPY sshd_config /etc/ssh/sshd_config

# http://stackoverflow.com/questions/22547939/docker-gitlab-container-ssh-git-login-error
RUN sed -i '/session    required     pam_loginuid.so/d' /etc/pam.d/sshd

COPY setup.sh /
RUN chmod +x /setup.sh

COPY run-signup.sh /
RUN chmod +x /run-signup.sh

ENTRYPOINT ["/run-signup.sh", "/setup.sh"]

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
