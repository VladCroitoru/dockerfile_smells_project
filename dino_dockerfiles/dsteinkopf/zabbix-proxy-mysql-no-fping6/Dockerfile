FROM zabbix/zabbix-proxy-mysql:ubuntu-latest

USER root

RUN sed -i 's/update_config_var .ZBX_CONFIG .Fping6Location./update_config_var $ZBX_CONFIG "Fping6Location" "\/doesnotexist"/' /usr/bin/docker-entrypoint.sh
RUN sed -i 's/update_config_var .ZBX_CONFIG .FpingLocation./update_config_var $ZBX_CONFIG "FpingLocation" "\/usr\/bin\/fping"/' /usr/bin/docker-entrypoint.sh


USER 1997
