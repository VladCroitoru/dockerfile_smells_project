FROM valtri/docker-midpoint:3.7.2
MAINTAINER František Dvořák <valtri@civ.zcu.cz>

ENV v 3.7.2
ENV schema config/sql/_all/mysql-3.7-all.sql

WORKDIR /root

RUN apt-get update && apt-get install -y --no-install-recommends \
    mariadb-server \
&& rm -rf /var/lib/apt/lists/*

COPY midpoint.cnf /etc/mysql/conf.d/
RUN wget -nv https://raw.githubusercontent.com/Evolveum/midpoint/v${v}/${schema}
RUN pass='changeit' \
&& service mysql start \
&& mysql -e "CREATE DATABASE midpoint CHARACTER SET utf8 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin DEFAULT COLLATE utf8_bin" \
&& mysql -e "GRANT ALL ON midpoint.* TO midpoint@localhost IDENTIFIED BY '${pass}'" \
&& mysql -u midpoint -p${pass} midpoint < `basename ${schema}`

RUN xmlstarlet ed --inplace --update '/configuration/midpoint/repository' --value '' /var/opt/midpoint/config.xml
COPY config-repo.txt .
RUN while read key value; do xmlstarlet ed --inplace --subnode /configuration/midpoint/repository --type elem --name ${key} --value ${value} /var/opt/midpoint/config.xml; done < config-repo.txt
RUN rm config-repo.txt

RUN rm -fv /var/opt/midpoint/midpoint*.db

RUN mv /docker-entry.sh /docker-entry-base.sh
COPY docker-entry.sh /
