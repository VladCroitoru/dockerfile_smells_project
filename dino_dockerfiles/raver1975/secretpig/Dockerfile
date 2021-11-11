FROM ubuntu:15.04

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y  software-properties-common && \
    add-apt-repository ppa:webupd8team/java -y && \
    apt-get update && \
    echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y oracle-java8-installer && \
    apt-get clean
RUN add-apt-repository universe
RUN apt-get update && apt-get install -y \
    apache2 \
    curl \
    git \
    libapache2-mod-php5 \
    php5 \
    php5-mcrypt \
    php5-mysql \
    python3.4 \
    python3-pip
COPY ./src /usr/src/myapp
WORKDIR /usr/src/myapp
RUN javac Main.java
RUN pip3 install -r requirements.txt
CMD ["java", "Main"]