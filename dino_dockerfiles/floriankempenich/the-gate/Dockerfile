FROM nginx


## INSTALL TOOLS ###############################################################
################################################################################
# `inotifywait` => Watching Certificates
# `openssl`     => Generate Temp Certificates
# `ps`          => Debugging
RUN apt-get update && apt-get install -y \
    inotify-tools \
    procps \
    openssl \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
## END - INSTALL TOOLS #########################################################
################################################################################


## ADD SCRIPTS #################################################################
################################################################################
RUN mkdir /scripts
ADD ./docker_image/scripts/reload_nginx_on_file_change.sh              /scripts
ADD ./docker_image/scripts/start_nginx_and_reload_on_config_changes.sh /scripts
################################################################################
## END - ADD SCRIPTS ###########################################################


## ADD `NGINX` CONFIG ##########################################################
################################################################################
WORKDIR /etc/nginx/

# Base configuration
RUN rm ./nginx.conf
ADD ./docker_image/nginx_conf/nginx.conf         .
ADD ./docker_image/nginx_conf/services.base.conf .
################################################################################
## END - ADD `NGINX` CONFIG ####################################################


## START COMMAND ###############################################################
################################################################################
WORKDIR /scripts
CMD ["./start_nginx_and_reload_on_config_changes.sh"]
