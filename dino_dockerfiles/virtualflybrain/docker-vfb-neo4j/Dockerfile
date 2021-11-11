FROM neo4j:2.3-enterprise

RUN apt-get -y update && apt-get -y install ssh


# Location of config files (separate in v2)
ENV NEOCONF="/var/lib/neo4j/conf/neo4j.properties"
ENV NEOSERCONF="/var/lib/neo4j/conf/neo4j-server.properties"
# Read_only setting:
ENV NEO4J_dbms_read__only=false
ENV NEO4J_read__only=false
# Default is open access change bellow to require
ENV NEO4J_dbms_security_auth__enabled=false
ENV NEO4J_AUTH=neo4j/password
# Enable upgrading of DB:
ENV NEO4J_ALLOW_STORE_UPGRADE=true
ENV NEO4J_dbms_allowFormatMigration=true
# Max memory size (typically half the default):
ENV NEO4J_dbms_memory_heap_maxSize=10G
#Enable full logging:
ENV NEO4J_org_neo4j_server_http_log_enabled=true
ENV NEO4J_dbms_logs_query_enabled=true
ENV NEO4J_dbms_logs_query_allocation__logging__enabled=true
ENV NEO4J_dbms_logs_query_time__logging__enabled=true
# Log all queries that take longer then (seconds):
ENV NEO4J_dbms_logs_query_threshold=0
# Accept Neo4j license:
ENV NEO4J_ACCEPT_LICENSE_AGREEMENT=yes

ENV NEO4J_CACHE_MEMORY=2G
ENV NEO4J_HEAP_MEMORY=5120

ENV NEOREADONLY=true

COPY neo4j /etc/default/neo4j 
COPY limits.conf /etc/security/limits.conf

RUN sed -i s/wrapper.java.initmemory=512/wrapper.java.initmemory=1024/ /var/lib/neo4j/conf/neo4j-wrapper.conf
RUN sed -i s/wrapper.java.maxmemory=512/wrapper.java.maxmemory=5120/ /var/lib/neo4j/conf/neo4j-wrapper.conf
 
RUN sed -i s/dbms.security.auth_enabled=true/dbms.security.auth_enabled=false/ ${NEOSERCONF} && \
sed -i s/#dbms.security.auth_enabled=false/dbms.security.auth_enabled=false/ ${NEOSERCONF} && \
echo '' >> ${NEOSERCONF} && \
echo 'read_only=true' >> ${NEOSERCONF} && \
sed -i s/#allow_store_upgrade=true/allow_store_upgrade=true/ ${NEOCONF} && \
sed -i s/#dbms.allow_format_migration=true/dbms.allow_format_migration=true/ ${NEOCONF} && \
sed -i s/#dbms.logs.query.enabled=true/dbms.logs.query.enabled=true/ ${NEOCONF} && \
sed -i 's|#dbms.security.load_csv_file_url_root=data/import|dbms.security.load_csv_file_url_root=/import|' ${NEOCONF} && \
echo 'dbms.logs.query.parameter_logging_enabled=true' >> ${NEOSERCONF} && \
echo 'dbms.jvm.additional=-Xss6M' >> ${NEOSERCONF}
