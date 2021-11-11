# elFinder on nginx and php on MapR PACC
#
# VERSION 0.1 - not for production, use at own risk
#

#
# Using mapr-pacc-nginx-docker as the base image
# For specific versions check: https://hub.docker.com/r/mkieboom/mapr-pacc-nginx-docker/
FROM mkieboom/mapr-pacc-nginx-docker

RUN yum install -y unzip

# Download elFinder
RUN curl -L -O https://github.com/Studio-42/elFinder/archive/2.1.31.zip && \
    unzip *.zip && \
    rm -f *.zip

# Install elFinder in the nginx html folder (/usr/share/nginx/html)
RUN mv elFinder-* elFinder && \
    chown -R nginx:nginx elFinder && \
    mv elFinder/php/connector.minimal.php-dist elFinder/php/connector.minimal.php && \
    rm -rf elFinder/files && \
    ln -s /mapr ./elFinder/files && \
    mv elFinder/* /usr/share/nginx/html/ && \
    rm -rf elFinder && \
    rm -rf /usr/share/nginx/html/index.html && \
    mv /usr/share/nginx/html/elfinder.html /usr/share/nginx/html/index.html

# Upload a custom configuration file to point elFinder to /mapr/
COPY connector.php /usr/share/nginx/html/php/connector.minimal.php 
RUN chown nginx:nginx /usr/share/nginx/html/php/connector.minimal.php 

EXPOSE 80

# Add the launch script which checks if the /mapr mountpoint is available in the container
ADD launch.sh /launch.sh
RUN sudo chmod +x /launch.sh

# Launch nginx, php and elFinder
CMD /launch.sh
#CMD /bin/bash
