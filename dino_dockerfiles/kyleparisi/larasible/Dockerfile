FROM ubuntu:18.04
RUN apt-get update && apt-get install sudo git -y
ADD . larasible
WORKDIR larasible
RUN ./provision.sh
WORKDIR /var/www/default
EXPOSE 80
ENTRYPOINT ["/bin/bash", "/larasible/run.sh"]
