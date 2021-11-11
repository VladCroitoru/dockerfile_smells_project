#titan/gremlin server

FROM java:8

MAINTAINER jdietrich

RUN apt-get update && apt-get install -y \
	maven 

WORKDIR /opt

RUN git clone https://github.com/awslabs/dynamodb-titan-storage-backend.git

WORKDIR /opt/dynamodb-titan-storage-backend

RUN mvn install

RUN src/test/resources/install-gremlin-server.sh

WORKDIR /opt/dynamodb-titan-storage-backend/server/dynamodb-titan100-storage-backend-1.0.0-hadoop1

ADD conf /conf

EXPOSE 8182

ENTRYPOINT ["bin/gremlin-server.sh"]

CMD ["/conf/gremlin-server-local.yaml"]
