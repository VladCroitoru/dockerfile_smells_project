FROM ubuntu:16.04
MAINTAINER Bernd KLAUS "https://berndklaus.at"

ADD run.sh /usr/sbin/run.sh
RUN apt-get update && apt-get upgrade -y && apt-get install -y openssh-server openssh-client nano \
    curl wget zip unzip apt-transport-https ca-certificates curl software-properties-common libpam-google-authenticator \
 && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \
 && apt-key fingerprint 0EBFCD88 \
 && add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable" \
 && apt-get update && apt-get install docker-ce --no-install-recommends -y && apt-get clean
 
ENV PASSWORD root

RUN chmod 755 /usr/sbin/run.sh && mkdir -p /var/run/sshd /root/.ssh \
 && sed -i 's/ChallengeResponseAuthentication no/ChallengeResponseAuthentication yes/' /etc/ssh/sshd_config \
 && echo "auth required pam_google_authenticator.so" >> /etc/pam.d/sshd \
 && echo 'root:'$PASSWORD |chpasswd \
 && sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config


EXPOSE 22

ENTRYPOINT ["/usr/sbin/run.sh"]
CMD ["/usr/sbin/sshd", "-D"]
