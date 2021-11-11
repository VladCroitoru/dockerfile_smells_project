FROM        debian:wheezy

# basic build image
ADD			installDeps.sh /opt/installDeps.sh
RUN         apt-get update && bash /opt/installDeps.sh

# build and install
ADD			install.sh /opt/install.sh
ADD			cleanup.sh /opt/cleanup.sh
RUN			bash /opt/install.sh
RUN			printf "\n\ndaemon off;\n" >> /etc/nginx/nginx.conf
ADD			pagespeedBaseConf.conf /etc/nginx/pageSpeed
ADD			pagespeedBaseConf.conf /opt/
RUN			printf '#!/bin/bash\n/usr/sbin/nginx -g "daemon off;"\n' > /opt/nginx.sh && chmod ugo+x /opt/nginx.sh

ENTRYPOINT	/opt/nginx.sh
EXPOSE      80
