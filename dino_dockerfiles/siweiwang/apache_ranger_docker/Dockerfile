FROM siweiwang/apache_ranger_base

# Install mysql for mysql client
RUN yum clean all -y && \
      yum update -y && \
      yum -y install mysql

# Download SQL connetor JAR
RUN wget -P /opt/ranger https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.41.tar.gz && \
     tar -xvf /opt/ranger/mysql-connector-java-5.1.41.tar.gz -C /opt/ranger

# Copy over the install.properies file
RUN mkdir /opt/ranger_home && \
     cp /opt/ranger/apache-ranger-0.7.0/target/ranger-0.7.0-admin.tar.gz /opt/ranger_home && \
      tar -zxvf /opt/ranger_home/ranger-0.7.0-admin.tar.gz -C /opt/ranger_home

WORKDIR /opt/ranger_home/ranger-0.7.0-admin

ADD ./install.properties install.properties
ADD ./bootstrap.sh .
ADD ./ranger.sql .

# Change permission
RUN chmod 755 ./bootstrap.sh

CMD ./bootstrap.sh

