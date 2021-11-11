FROM payara/server-full
MAINTAINER Axel Ballarin, moonsandmore.com

ARG DB_HOST=mysql
ARG DB_NAME=airport
ARG DB_USER=airport
ARG DB_PASSWORD=airport

ARG AS_ADMIN_PASSWORD=admin
ARG AS_MASTER_PASSWORD=master

ADD mysql-connector-java.jar ${PAYARA_PATH}/glassfish/lib/

RUN echo "AS_ADMIN_PASSWORD=${AS_ADMIN_PASSWORD}\n\
AS_MASTER_PASSWORD=${AS_MASTER_PASSWORD}\n\
EOF\n"\
>> /opt/gfpwdfile
RUN chmod 600 /opt/gfpwdfile

RUN echo | $PAYARA_PATH/bin/asadmin --user=admin --passwordfile=/opt/gfpwdfile create-domain frms-planning

RUN \
 ${PAYARA_PATH}/bin/asadmin start-domain frms-planning && \
 ${PAYARA_PATH}/bin/asadmin --user=admin --passwordfile=/opt/gfpwdfile enable-secure-admin && \
 ${PAYARA_PATH}/bin/asadmin restart-domain frms-planning && \
 ${PAYARA_PATH}/bin/asadmin --user=admin --passwordfile=/opt/gfpwdfile create-jdbc-connection-pool \
    --datasourceclassname=com.mysql.jdbc.jdbc2.optional.MysqlDataSource \
    --restype=javax.sql.DataSource \
    --property=Url=jdbc\\:${DB_HOST}\\://mysql\\:3306/${DB_NAME}:user=${DB_USER}:password=${DB_PASSWORD} AirportPool && \
 ${PAYARA_PATH}/bin/asadmin --user=admin --passwordfile=/opt/gfpwdfile create-jdbc-resource --connectionpoolid=AirportPool jdbc/airport && \
 ${PAYARA_PATH}/bin/asadmin --user=admin --passwordfile=/opt/gfpwdfile create-auth-realm --classname=com.sun.enterprise.security.auth.realm.jdbc.JDBCRealm \
    --property=jaas-context=jdbcRealm:datasource-jndi=jdbc/airport:user-table=${DB_NAME}.user:user-name-column=email:password-column=password:group-table=${DB_NAME}.user_role:group-name-column=role_name:digestrealm-password-enc-algorithm=SHA-256:assign-groups=USER,ADMIN airportRealm

ENTRYPOINT ${PAYARA_PATH}/bin/asadmin --user admin --passwordfile /opt/gfpwdfile start-domain --verbose frms-planning
