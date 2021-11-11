FROM mbentley/teamspeak

# Setting SQL connection environment variables
ENV TS_DB_HOST 127.0.0.1
ENV TS_DB_PORT 3306
ENV TS_DB_NAME teamspeak
ENV TS_DB_USER teamspeak
ENV TS_DB_PASSWORD teamspeak

USER root

# Adding SQL configuration files
ADD build/ts3db_sql.ini /opt/teamspeak/ts3db_sql.ini
ADD build/ts3server.ini /opt/teamspeak/ts3server.ini
ADD build/docker-entrypoint.sh /opt/teamspeak/docker-entrypoint.sh

RUN cp /opt/teamspeak/redist/libmariadb.so.2 /opt/teamspeak/libmariadb.so.2

# Applying user permissions
RUN chmod u+x /opt/teamspeak/docker-entrypoint.sh
RUN chown -R teamspeak: /opt/teamspeak/

USER teamspeak

ENTRYPOINT ["/opt/teamspeak/docker-entrypoint.sh"]
