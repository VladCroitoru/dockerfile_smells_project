FROM nginx
MAINTAINER kaiyadavenport@gmail.com
RUN apt-get update && apt-get install -y apache2-utils
COPY ./run.sh /run.sh
ENTRYPOINT ["bash", "/run.sh"]