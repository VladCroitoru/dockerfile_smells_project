FROM node:6

RUN apt-get update
RUN apt-get install -y libaio1 unzip
RUN apt-get clean -y

# Oracle instantclient
ADD instantclient-basic-linux.x64-12.1.0.2.0.zip /tmp/
ADD instantclient-sdk-linux.x64-12.1.0.2.0.zip /tmp/

RUN unzip /tmp/instantclient-basic-linux.x64-12.1.0.2.0.zip -d /usr/local/
RUN unzip /tmp/instantclient-sdk-linux.x64-12.1.0.2.0.zip -d /usr/local/

RUN ln -s /usr/local/instantclient_12_1 /usr/local/instantclient
RUN ln -s /usr/local/instantclient/libclntsh.so.12.1 /usr/local/instantclient/libclntsh.so

ENV LD_LIBRARY_PATH /usr/local/instantclient
ENV OCI_LIB_DIR /usr/local/instantclient
ENV OCI_INC_DIR /usr/local/instantclient/sdk/include

CMD [ "node" ]
