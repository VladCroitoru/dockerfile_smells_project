FROM alpine

RUN apk update && apk add openssh pwgen
RUN sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config \
	&& sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config \
	&& sed -i "s/#PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config

ADD set_root_pw.sh /set_root_pw.sh
ADD run.sh /run.sh
RUN chmod +x /*.sh

# ENV ROOT_PASS **RANDOM**

ENV PUBLIC_SSH_KEYS **None**

VOLUME /user

EXPOSE 22
CMD ["sh", "/run.sh"]
