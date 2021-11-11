FROM mysql:5.6
MAINTAINER Sander Dijkhuis <mail@sanderdijkhuis.nl>

ADD docker-mysql-initialize.sh /mysql-initialize.sh
RUN chmod +x /mysql-initialize.sh

CMD ["/mysql-initialize.sh"]