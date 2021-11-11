FROM jenkinsci/jenkins 
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/executors.groovy
USER root
# TODO docker-compose oracle-java9-installer oracle-java9-set-default oracle-java9-unlimited-jce-policy php-cli
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
 apt-transport-https \
 aptitude \
 ca-certificates-java \
 software-properties-common \
 && apt-add-repository -y non-free \
 && apt-add-repository -y contrib \
 && apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys \
 58118E89F3A912897C070ADBF76221572C52609D \
 && apt-add-repository -y "deb https://apt.dockerproject.org/repo debian-jessie main" \
 && aptitude update \
 && DEBIAN_FRONTEND=noninteractive aptitude --with-recommends full-upgrade -y \
 && DEBIAN_FRONTEND=noninteractive aptitude --with-recommends -y install \
 ant \
 binfmt-support \
 default-jdk \
 docker.io \
 git \
 gradle \
 gradle-doc \
 maven \
 mercurial \
 phing \
 php5-cli \
 scala \
 scala-doc \
 doxygen \
 doxygen-doc \
 doxygen-latex \
 graphviz \
 graphviz-doc \
 gsfonts
USER jenkins
ENV CURL_CONNECTION_TIMEOUT 60
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt
