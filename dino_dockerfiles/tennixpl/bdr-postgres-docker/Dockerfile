FROM centos:26062017-updated

################################################
## Environment Variables #######################
################################################
ENV POSTGRES_PASSWORD=postrgres
ENV POSTGRES_USER=postgres
ENV PGDATA=/database
ENV MY_IP_LOC=localhost
ENV MY_PORT=5432
ENV CONFIG_FILES_LOC=/configs_to_ingest
RUN mkdir $CONFIG_FILES_LOC


################################################
## Start specific BDR instructions
## bdr-project.org/docs/stable/quickstart-starting.html
################################################

##################################
## Install bdr repository
##################################
RUN yum install -y http://packages.2ndquadrant.com/postgresql-bdr94-2ndquadrant/yum-repo-rpms/postgresql-bdr94-2ndquadrant-redhat-latest.noarch.rpm

#############################################################
## Enable the potgress repo for future upgrades or updates ##
#############################################################
RUN yum install -y https://download.postgresql.org/pub/repos/yum/9.4/redhat/rhel-7-x86_64/pgdg-centos94-9.4-3.noarch.rpm

###########################################
## Enable the EPEL repo for dependencies ##
###########################################
RUN yum install -y http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-9.noarch.rpm
RUN yum check-update -y

RUN yum install -y postgresql-bdr94-bdr

RUN su -l postgres -c "export PATH=/usr/pgsql-9.4/bin:$PATH"
RUN export PATH=/usr/pgsql-9.4/bin:$PATH

RUN mkdir /database
RUN chown postgres:postgres $PGDATA
RUN chown postgres:postgres $CONFIG_FILES_LOC

RUN su -l postgres -c "/usr/pgsql-9.4/bin/initdb -D $PGDATA -A trust -U postgres"
ADD docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/bin/bash"]
