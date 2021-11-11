FROM ubuntu

MAINTAINER Gajo Petrovic, gajop01@gmail.com

#RUN echo 'deb http://archive.ubuntu.com/ubuntu precise main universe' > /etc/apt/sources.list

RUN apt-get update -y -q
RUN apt-get install -y -q p7zip-full
RUN apt-get install -y -q wget
RUN apt-get install -y -q default-jdk
RUN apt-get install -y -q unzip

RUN mkdir botrunner_folder
WORKDIR botrunner_folder

RUN wget --quiet -O spring.7z 			https://springrts.com/dl/buildbot/default/master/100.0/linux64/spring_100.0_minimal-portable-linux64-static.7z 
RUN wget --quiet -O spring_src.tar.gz 	https://springrts.com/dl/buildbot/default/master/100.0/source/spring_100.0_src.tar.gz
RUN wget --quiet -O botrunner.zip https://github.com/gajop/botrunner/archive/master.zip
RUN 7z x -ospring spring.7z
RUN tar xvf spring_src.tar.gz

# Add maps/games
RUN mkdir -p /root/.config/spring
WORKDIR /root/.config/spring

RUN mkdir -p maps
WORKDIR maps
RUN wget --quiet http://spring1.admin-box.com/downloads/spring/spring-maps/TitanDuel.sd7
RUN wget --quiet http://spring1.admin-box.com/downloads/spring/spring-maps/Eye_Of_Horus_v2.sd7
RUN wget --quiet http://api.springfiles.com/files/maps/intersection_v3.sd7
RUN wget --quiet http://spring1.admin-box.com/downloads/spring/spring-maps/RedComet.sd7
RUN wget --quiet http://spring1.admin-box.com/downloads/spring/spring-maps/Barren.sd7
RUN wget --quiet http://spring1.admin-box.com/downloads/spring/spring-maps/Bandit_plains_v1.sd7
RUN wget --quiet http://api.springfiles.com/files/maps/wanderlust_v01.sd7
RUN wget --quiet http://spring1.admin-box.com/maps/victoria_crater_v2.1.sd7
WORKDIR ..

RUN mkdir -p games
WORKDIR games
RUN wget --quiet -O aitourney.zip https://github.com/Anarchid/Zero-K/archive/aitourney.zip  
RUN unzip aitourney.zip
RUN mv Zero-K-aitourney ZK-aitourney.sdd
WORKDIR ..

RUN mkdir -p AI/Skirmish
WORKDIR AI/Skirmish
RUN wget -O ZKGBAI_0.4.7z --quiet https://www.dropbox.com/s/fdzdj1s52dhujbw/ZKGBAI_0.4.7z?dl=1
RUN 7z x ZKGBAI_0.4.7z
RUN wget -O CircuitAI_0_7_6_4.zip --quiet https://www.dropbox.com/s/0ae5wbevyubfmqp/CircuitAI_0_7_6_4.zip?dl=1
RUN unzip CircuitAI_0_7_6_4.zip
RUN wget -O zkai.7z --quiet https://dl.dropboxusercontent.com/u/19320633/zkai.7z
RUN 7z x zkai.7z
WORKDIR ..

# Configure botrunner
WORKDIR /botrunner_folder
RUN unzip -d botrunner botrunner.zip
RUN mv botrunner/botrunner-master/* botrunner/
RUN mv botrunner/botrunner-master/.gitignore* botrunner/ #ugh
RUN rmdir botrunner/botrunner-master
WORKDIR botrunner
ADD config.py /botrunner_folder/botrunner/botrunner/config.py
WORKDIR ..

WORKDIR ..

RUN apt-get install -y -q python3-psutil

CMD ["/botrunner_folder/botrunner/botrunner/botrunner.py"]