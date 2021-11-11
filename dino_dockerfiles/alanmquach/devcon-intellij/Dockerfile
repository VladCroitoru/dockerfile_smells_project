FROM alanmquach/devcon-wm:latest

MAINTAINER Alan Quach <integsrtite@gmail.com>

# JDK
RUN apt-get install -y software-properties-common \
    && apt-add-repository -y ppa:webupd8team/java \
    && echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections \
    && apt-get update && apt-get install -y oracle-java8-installer oracle-java8-unlimited-jce-policy
# RUN add-apt-repository -y ppa:openjdk-r/ppa
# RUN apt-get update && apt-get install -y openjdk-8-jdk

# IntelliJ
RUN wget https://download.jetbrains.com/idea/ideaIC-2016.2.5.tar.gz -O /tmp/intellij.tar.gz -q \
    && echo 'Installing IntelliJ IDEA' \
    && mkdir -p /opt/intellij \
    && tar -xf /tmp/intellij.tar.gz --strip-components=1 -C /opt/intellij \
    && rm /tmp/intellij.tar.gz \
    && echo -ne '#!/bin/bash'"\n\nexec /opt/intellij/bin/idea.sh\n" > /usr/local/bin/intellij \
    && chmod a+x /usr/local/bin/intellij

CMD ["/usr/sbin/sshd", "-D"]

