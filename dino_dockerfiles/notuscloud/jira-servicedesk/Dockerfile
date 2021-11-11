FROM centos:7.3.1611

ENV INSTALL_PATH=/opt/atlassian/jira
ENV DATA_PATH=/var/atlassian/jira

# Fetch Install binary
RUN yum install -y wget bzip2 rsync
RUN mkdir /install
WORKDIR /install
RUN wget https://www.atlassian.com/software/jira/downloads/binary/atlassian-servicedesk-3.3.2-x64.bin

# Add the entrypoint
COPY entrypoint.sh /install/.
COPY install.sh /install/.
RUN chmod 755 /install/entrypoint.sh
RUN chmod 755 /install/install.sh

# Prepare the system
RUN sh /install/install.sh

# Volumes and Ports
VOLUME ["/opt/atlassian/jira", "/var/atlassian/jira"]
EXPOSE 8080 8005

# Entrypoint
ENTRYPOINT ["/install/entrypoint.sh"]
