FROM python:3

ENV VER=${VER:-master} \
    REPO=https://github.com/twhtanghk/pam_oauth2 \
    APP=/usr/src/app

WORKDIR $APP

# sshd
RUN apt-get update && \
    apt-get install -y ssh && \
    mkdir /var/run/sshd

# pam_oauth2
RUN apt-get install -y git sudo libpam0g-dev && \
    git clone -b $VER $REPO $APP && \
    make install && \
    sed 's/^\(passwd:.*\)$/\1 oauth2/g' </etc/nsswitch.conf >/tmp/nsswitch.conf && \
    mv /tmp/nsswitch.conf /etc && \
    pip install -r python/requirements.txt && \
    cp -a pam/pam.d/* /etc/pam.d

# clean
RUN apt-get clean
EXPOSE 22

CMD ./entrypoint.sh
