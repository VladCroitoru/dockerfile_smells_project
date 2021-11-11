# Base image.  You can pull from Docker Hub.  Codenvy
# provides a series of tested base images that include 
# Web Shell, installed utilities, and language support.
# You can browse our images in Docker Hub or at
# github.com/codenvy/dockerfiles. The shellinabox image
# provides core Linux utilities and terminal access to runner.
FROM 			codenvy/shellinabox

# set environment variables
ENV 			DEBIAN_FRONTEND noninteractive
ENV 			APACHE_RUN_USER www-data
ENV 			APACHE_RUN_GROUP www-data
ENV 			APACHE_LOG_DIR /var/log/apache2
ENV 			SITE_DIR /var/www/html

# make a temp dir 
RUN         mkdir -p /home/user/workspace

# set the working directory
WORKDIR     /home/user

# update packages and install apt-utils package
RUN         echo y|sudo apt-get update
RUN         echo y|sudo apt-get install apt-utils

# install and configure Apache
RUN			sudo apt-get update && \
    			sudo apt-get -y install apache2 && \
    			sudo rm -R $SITE_DIR/* && \
    			echo "ServerName localhost" | sudo tee -a /etc/apache2/apache2.conf

# expose and listen to port 80
# this is so we can connect to the docker image using a web browser
EXPOSE 		80
ENV			CODENVY_APP_PORT_80_HTTP 80

# install Haxe and the Haxe libs we need
RUN         wget -qO-  "http://www.openfl.org/builds/haxe/haxe-3.1.3-linux-installer.tar.gz"| tar -zx -C  /home/user/workspace
RUN         echo y|/home/user/workspace/install-haxe.sh>/dev/null 2>&1
RUN         haxelib install hxcpp
RUN         haxelib install lime
RUN         echo y|haxelib run lime setup
RUN         lime install openfl
RUN         echo y|haxelib run openfl setup
RUN         haxelib install haxeui
