#FROM bartt/ubuntu-base
FROM phusion/baseimage:0.9.17
MAINTAINER nmcaullay <nmcaullay@gmail.com>

# Set correct environment variables.
ENV HOME /root

#Create the pocketmine user
RUN useradd -u 1000 -g 100 pocketmine

RUN apt-get -y update
RUN apt-get -y install python3-yaml wget

#Create the home folder, set the permissions
RUN mkdir /pocketmine
#RUN mkdir /pocketmine-data

RUN cd /pocketmine && curl -sL http://get.pocketmine.net/ | bash -s - -r -v development
RUN mv /pocketmine/PocketMine-MP.phar /pocketmine/PocketMine-MP-orig.phar
#RUN wget http://jenkins.pocketmine.net/job/PocketMine-MP-Bleeding/30/artifact/PocketMine-MP_1.6dev-30_mcpe-0.12_86c11986_API-1.13.0.phar -O /pocketmine/PocketMine-MP.phar
#RUN wget http://jenkins.pocketmine.net/job/PocketMine-MP-Bleeding/43/artifact/PocketMine-MP_1.6dev-43_0.12-items_84be56fe_API-1.13.0.phar -O /pocketmine/PocketMine-MP.phar
RUN wget http://jenkins.pocketmine.net/job/PocketMine-MP-Bleeding/48/artifact/PocketMine-MP_1.6dev-48_mcpe-0.12_f9d7e204_API-1.13.0.phar -O /pocketmine/PocketMine-MP.phar

COPY source/eula.txt /pocketmine/eula.txt
#RUN chown -R pocketmine:100 /pocketmine/eula.txt

# Change user to pocketmine
RUN chown -R pocketmine:100 /pocketmine
#RUN chown -R pocketmine:100 /pocketmine-data

#USER pocketmine

WORKDIR /pocketmine

#Expose the port from the container
EXPOSE 19132

CMD ["./start.sh", "--no-wizard", "--enable-rcon=on", "--data-path=/pocketmine"]
#CMD ["/pocketmine/bin/php5/bin/php", "/pocketmine/PocketMine-MP-new.phar"]

#VOLUME /pocketmine
