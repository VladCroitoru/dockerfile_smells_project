FROM ubuntu:14.04

RUN apt-get update &&\
    apt-get install ssh autossh -y

CMD autossh $SSH_USER@$SSH_HOST -L *:$TUNNEL_PORT:$TARGET_HOST:$TARGET_PORT -N -v -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no $SSH_OPTIONS
