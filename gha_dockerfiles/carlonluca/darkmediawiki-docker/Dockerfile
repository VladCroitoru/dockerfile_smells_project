FROM mediawiki:1.36.2
ADD https://github.com/carlonluca/DarkVector/archive/refs/heads/master.zip /var/www/html/skins/
WORKDIR /var/www/html/skins/
RUN apt-get update && apt-get install -y unzip
RUN unzip master.zip
RUN mv DarkVector-master DarkVector
RUN apt-get remove -y unzip && apt-get clean
