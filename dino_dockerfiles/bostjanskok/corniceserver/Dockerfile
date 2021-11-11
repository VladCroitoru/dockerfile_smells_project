
FROM python:3.5-alpine

USER root

RUN pip install --upgrade pip \
 && pip3 install cornice && pip3 install Waitress \
 && pip3 install sqlalchemy && pip3 install zope.sqlalchemy \
 && pip3 install alembic
RUN apk update;apk add postgresql-dev;apk add gcc
RUN apk add python3-dev;apk add  musl-dev;apk add libffi-dev
RUN pip3 install psycopg2;pip3 install bcrypt
RUN pip3 install pyramid_tm;pip3 install PyJWT;pip3 install pyramid_jwt

RUN apk del gcc;apk del python3-dev;apk del musl-dev;apk del libffi-dev
RUN apk add libffi

RUN apk add openssh
RUN mkdir /var/run/sshd
RUN ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa
RUN sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config && sed -i "s/#AuthorizedKeysFile/AuthorizedKeysFile/g" /etc/ssh/sshd_config

RUN echo 'root:screencast' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config


ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"
