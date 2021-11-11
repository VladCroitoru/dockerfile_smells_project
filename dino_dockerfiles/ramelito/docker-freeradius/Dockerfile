FROM ansible/ubuntu14.04-ansible:latest
MAINTAINER Anton Komarov anton.komarov@gmail.com

ENV MYSQL_RADIUS_USER 		raduser
ENV MYSQL_RADIUS_USER_PASSWORD	radpass
ENV RADIUS_SECRET		secret123
ENV FREERADIUS_VERSION 		"2.2.5"

ADD ansible /opt/ansible
WORKDIR /opt/ansible

RUN ansible-playbook site.yml -c local

EXPOSE 1812/udp 1813/udp

VOLUME /etc/freeradius

ENTRYPOINT ["./entrypoint.sh"]
CMD ["freeradius", "-X"]
