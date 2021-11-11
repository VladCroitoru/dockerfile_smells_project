# Test
FROM       appcontainers/centos66
MAINTAINER Jaime Valero <jaimevalero78@yahoo.es>
LABEL      Description="Synchronize user data from LDAP to Itop" Version="0.4.36"

# Install dependencies for repo
RUN yum install    -y mysql-server nc openldap-clients php php-common php-pdo php-cli php-mysql
RUN /etc/init.d/mysqld start 

# Get git repos
RUN mkdir -p /root/scripts/itop-docker/config
RUN yum install -y git
RUN yum clean all
RUN cd /root/scripts &&  git clone "https://github.com/jaimevalero78/itop-utilities"

# Entrypoint
CMD ["/bin/bash", "/root/scripts/itop-docker/startup.sh"]

# Start scripts
ADD ./startup.sh                  /root/scripts/itop-docker/
ADD ./root/scripts/itop-docker/   /root/scripts/itop-docker/

# Permissions
RUN chmod +x /root/scripts/itop-docker/*.{php,sh} 
RUN find root/scripts/itop-docker/ -type f 
RUN touch /root/scripts/itop-utilities/.credentials 
RUN ln -s /root/scripts/itop-utilities/.credentials /root/scripts/itop-docker/.credentials

EXPOSE 3306
VOLUME ["/var/tmp/" ]

