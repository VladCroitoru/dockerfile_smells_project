FROM dockerfile/java
MAINTAINER Todd Tyree <tatyree@gmail.com>

RUN mkdir /setup
ADD install.sh /setup/install.sh
RUN /setup/install.sh
ENTRYPOINT java -jar /srv/tika-server-1.6.jar -host 0.0.0.0

EXPOSE 9998
