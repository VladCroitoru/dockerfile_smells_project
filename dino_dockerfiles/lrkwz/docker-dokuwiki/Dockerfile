FROM nerka/docker-dokuwiki:alpine_edge_plugins_1.3

RUN apk update && apk add php7-json
RUN mkdir /plugins/
ADD https://github.com/turnermm/ckgedit/archive/master.zip /plugins/ckgedit.zip
#RUN unzip /master.zip -d /var/www/lib/plugins/ && mv /var/www/lib/plugins/ckgedit-master /var/www/lib/plugins/ckgedit && rm /master.zip
ADD https://github.com/LotarProject/dokuwiki-template-bootstrap3/zipball/master /plugins/bootstrap.zip
#RUN unzip /master -d /var/www/lib/tpl && mv /var/www/lib/tpl/LotarProject-dokuwiki-template-bootstrap3-cd91aa3 /var/www/lib/tpl/bootstrap3 && rm /master
ADD http://dev.xif.fr:7979/catlist/catlist-2017-01-11.zip /plugins/catlist.zip
#RUN unzip /catlist-2017-01-11.zip -d /var/www/lib/plugins/ && rm /catlist-2017-01-11.zip
ADD https://codeload.github.com/gturri/nspages/legacy.zip/master /plugins/nspages.zip
#RUN unzip -q /plugins/* -d /var/www/lib/plugins/ && rm -r /plugins
#RUN mv /var/www/lib/plugins

