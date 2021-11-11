FROM losinggeneration/w3af_gui:latest
MAINTAINER Harley Laue <losinggeneration@gmail.com>

# We need the local apt database up-to-date
RUN apt-get update -y

# Packages for remote usage
RUN apt-get install -y openssh-server supervisor
RUN mkdir -m755 -p /var/run/sshd

USER $USER
WORKDIR $HOME

# Add the SSH authorized key
RUN mkdir -m 700 .ssh
ADD ssh/id_rsa.pub $HOME/.ssh/authorized_keys

USER root

# Basically just runs sshd -D
ADD supervisord.conf /etc/supervisor/conf.d/sshd.conf

# Expose SSH
EXPOSE 22

ENTRYPOINT /usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf
