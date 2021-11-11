# Postgres on Kubernetes & MapR
# using the MapR Volume Driver Plugin for Kubernetes
#
# VERSION 0.1 - not for production, use at own risk
#

#
# Use a CentOS 7 image as the base
FROM centos

MAINTAINER mkieboom @ mapr.com

# Set Postgres environment variables, change to your liking
ENV PGDATA_LOCATION /postgres
ENV PG_DB mapr
ENV PG_GROUP mapr
ENV PG_USER mapr
ENV PG_PWD mapr
ENV PG_UID 5000
ENV PG_GID 5000

# Install Postgres
RUN yum install -y postgresql-server

# Add the launch script and make it executable
ADD ./launch.sh /launch.sh
RUN chmod +x /launch.sh

# Create the user and group to run the Postgres server
RUN groupadd -g $PG_GID $PG_GROUP
RUN useradd -u $PG_UID -g $PG_GID $PG_USER

# Expose the Postgres server port
EXPOSE 5432

CMD /launch.sh