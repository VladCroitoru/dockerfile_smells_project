FROM openjdk:8-jre

# Add the repo source
WORKDIR /usr/src
ADD ./zebedee-cms/target/dependency /usr/src/target/dependency
ADD ./zebedee-cms/target/classes /usr/src/target/classes

# Temporary: expose Elasticsearch
EXPOSE 9200

# Update the entry point script
ENTRYPOINT java -Xmx2048m \
          -Ddb_audit_url=$db_audit_url \
          -Ddb_audit_username=$db_audit_username \
          -Ddb_audit_password=$db_audit_password \
          -Drestolino.classes=target/classes \
          -Drestolino.packageprefix=com.github.onsdigital.zebedee.api \
          -cp "target/dependency/*:target/classes/" \
          com.github.davidcarboni.restolino.Main
