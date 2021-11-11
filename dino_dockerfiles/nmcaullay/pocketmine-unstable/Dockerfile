# Use the latest Ubuntu base image
FROM ubuntu:latest
MAINTAINER nmcaullay <nmcaullay@gmail.com>

# Silence debconf's endless prattle
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y \
    wget \
    python3-yaml
    
RUN wget http://jenkins.pocketmine.net/view/PHP/job/PHP-PocketMine-Linux/lastSuccessfulBuild/artifact/archive/linux/64bit/PHP_7.0.0RC3_x86-64_Linux.tar.gz -O /tmp/PHP.tar.gz

#RUN mkdir /usr/local/php7
RUN mkdir -p /var/lib/jenkins/jobs/PHP-PocketMine-Linux/workspace/compile/linux/64bit/
RUN tar -xvf /tmp/PHP.tar.gz -C /var/lib/jenkins/jobs/PHP-PocketMine-Linux/workspace/compile/linux/64bit/

# Get the PEAR, get the weakref
RUN wget http://pear.php.net/go-pear.phar -O /tmp/go-pear.phar
RUN /var/lib/jenkins/jobs/PHP-PocketMine-Linux/workspace/compile/linux/64bit/bin/php7/bin/php /tmp/go-pear.phar
RUN /var/lib/jenkins/jobs/PHP-PocketMine-Linux/workspace/compile/linux/64bit/bin/php7/bin/pear install pecl/weakref

#Create the pocketmine user
RUN useradd -u 1000 -g 100 pocketmine

#Create the home folder, set the permissions
RUN mkdir /pocketmine
RUN cd /pocketmine

#RUN wget http://jenkins.pocketmine.net/job/PocketMine-MP-Bleeding/48/artifact/PocketMine-MP_1.6dev-48_mcpe-0.12_f9d7e204_API-1.13.0.phar -O /pocketmine/PocketMine-MP.phar
#RUN wget http://jenkins.pocketmine.net/job/PocketMine-MP-PR/402/artifact/PocketMine-MP_1.7dev_PR-3672_94982d01_API-1.13.0.phar -O /pocketmine/PocketMine-MP.phar
RUN wget http://jenkins.pocketmine.net/view/PocketMine/job/PocketMine-MP-PR/414/artifact/PocketMine-MP_1.6.2dev_PR-3698_9bc88807_API-1.13.0.phar -O /pocketmine/PocketMine-MP.phar

COPY resources/eula.txt /pocketmine/eula.txt

# Change user to pocketmine
RUN chown -R pocketmine:100 /pocketmine

#Expose the port from the container
EXPOSE 19132

#CMD ["/usr/local/php7/bin/php7/bin/php", "/pocketmine/PocketMine-MP.phar"]
CMD ["/var/lib/jenkins/jobs/PHP-PocketMine-Linux/workspace/compile/linux/64bit/bin/php7/bin/php", "/pocketmine/PocketMine-MP.phar"]

