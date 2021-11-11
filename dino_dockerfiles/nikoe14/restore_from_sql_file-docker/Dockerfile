# DB - Restore - Dockerfile
#
# VERSION               0.0.1

FROM ubuntu

MAINTAINER Nicolás Espejo <nicolasgermanespejo@gmail.com>

RUN apt-get update && apt-get install -y mysql-client

#Entrypoint
ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]