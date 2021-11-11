# The base is my fork of tutum/wordpress-stackable in order to remove the VOLUME on /app/wp-content
# With VOLUME, you cannot make any modification https://github.com/docker/docker/issues/13117
# Try to config Wordpress use a different location for wp-content also failed
# https://wordpress.org/support/topic/cannot-properly-configure-wp_content_url
# https://github.com/tutumcloud/tutum-docker-wordpress-nosql/issues/23
FROM sunshineo/tutum-docker-wordpress-nosql:4.5.2

# The base does not have unzip unfortunately
RUN sudo apt-get update
RUN sudo apt-get install -qq zip
RUN sudo apt-get install -qq unzip

WORKDIR /app/wp-content

# Remove default plugins
RUN sudo rm -Rf ./plugins/akismet; exit 0
RUN sudo rm ./plugins/hello.php; exit 0

# Think of the below as: npm install bower
# https://github.com/sunshineo/wppatm
RUN curl -sSLO https://raw.githubusercontent.com/sunshineo/wppatm/master/install.sh
RUN chmod +x install.sh

# Think of these files as: bower.json
ADD plugins.txt ./
ADD themes.txt ./

# Think of the below as: bower install
RUN ./install.sh
