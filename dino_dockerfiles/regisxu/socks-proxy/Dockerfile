FROM alpine:3.4

RUN apk update && apk add openssh=7.2_p2-r3 && /usr/bin/ssh-keygen -A

RUN ssh-keygen -t rsa -P "" -f /root/.ssh/id_rsa

RUN cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

CMD /usr/sbin/sshd && ssh -ND 0.0.0.0:1080 -o StrictHostKeyChecking=no localhost
