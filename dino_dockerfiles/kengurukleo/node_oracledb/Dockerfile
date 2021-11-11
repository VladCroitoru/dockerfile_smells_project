# Pull Oracle Linux 7 image from Docker hub
FROM oraclelinux

# Install OS packages
RUN yum -y install unzip libaio gcc-c++ tar make curl \
&& useradd nodejs -p �$6$salt$ZjJzVKp5xtoIl7cfXqZe0mQjWeOpsV2pMiIYpWzkR4ExCBpPdT3mi3eXtG1MSawJnZfXFjBcq0UUmenLq1Cj//�

RUN curl -sSL https://nodejs.org/dist/v6.10.3/node-v6.10.3-linux-x64.tar.xz \
| tar -xJC /opt/
ENV PATH /opt/node-v6.10.3-linux-x64/bin:$PATH

# Add Oracle Instantclient
ADD instantclient-basic-linux.x64-12.1.0.2.0.zip /tmp/
ADD instantclient-sdk-linux.x64-12.1.0.2.0.zip /tmp/

RUN unzip -q /tmp/instantclient-basic-linux.x64-12.1.0.2.0.zip -d /opt/oracle/ \
&& unzip -q /tmp/instantclient-sdk-linux.x64-12.1.0.2.0.zip -d /opt/oracle/ \
&& mv /opt/oracle/instantclient_12_1 /opt/oracle/instantclient \
&& ln -s /opt/oracle/instantclient/libclntsh.so.12.1 /opt/oracle/instantclient/libclntsh.so\
&& rm /tmp/instantclient-*

ENV LD_LIBRARY_PATH /opt/oracle/instantclient

# Install the node-oracledb module as global module to Node.js using npm
RUN npm install -g oracledb

ENV NODE_PATH /opt/node-v6.10.3-linux-x64/lib/node_modules
