FROM delitescere/jdk
MAINTAINER mark.turner@collinsongroup.com

# Add the startup script
RUN mkdir -p /opt/scripts
COPY src/startup.sh /opt/scripts/
RUN chmod +x /opt/scripts/startup.sh

# Update & add git + svn
RUN apk update && apk add git subversion 

# Create installation location
# Create data & config folder
# Download TC and install to default location
# Add the MS SQL JDBC driver
RUN mkdir -p /var/lib/teamcity/config /var/lib/teamcity/lib/jdbc /tmp/jdbc && \
curl -L https://download.microsoft.com/download/0/2/A/02AAE597-3865-456C-AE7F-613F99F850A8/sqljdbc_4.2.6420.100_enu.tar.gz | tar -xz -C /tmp/jdbc sqljdbc_4.2/enu/sqljdbc4.jar && find /tmp/jdbc/sqljdbc_4.2/enu/ -name '*.jar' -exec mv {} /var/lib/teamcity/lib/jdbc \+ && rm -rf /tmp/jdbc && \
curl -L https://download.jetbrains.com/teamcity/TeamCity-9.1.3.tar.gz | tar -xz -C /opt

# Set configuration vars
ENV TEAMCITY_SERVER_MEM_OPTS -Xmx1024m -XX:MaxPermSize=270m

# Set the data folder for TeamCity and expose paths
ENV TEAMCITY_DATA_PATH /var/lib/teamcity
VOLUME /var/lib/teamcity/config
VOLUME /var/lib/teamcity/plugins
VOLUME /var/lib/teamcity/backup
VOLUME /var/lib/teamcity/lib
VOLUME /var/lib/teamcity/keys
VOLUME /opt/TeamCity/logs

# Expose the standard TeamCity port
EXPOSE 8111

# Run TeamCity
ENTRYPOINT ["/opt/scripts/startup.sh"]
