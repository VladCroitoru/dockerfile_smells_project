FROM openjdk:8-jre

RUN curl -sL https://deb.nodesource.com/setup_12.x -o /opt/nodesource_setup.sh
RUN bash /opt/nodesource_setup.sh
RUN apt-get install -y build-essential
RUN apt-get install -y nodejs

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - 
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update &&  apt-get install -y yarn

RUN yarn global add serverless typescript mocha tslint

RUN mkdir /var/dynamodb_local

WORKDIR /var/dynamodb_local

ENV DYNAMODB_VERSION=latest

ENV JAVA_OPTS=

RUN curl -O https://s3-us-west-2.amazonaws.com/dynamodb-local/dynamodb_local_${DYNAMODB_VERSION}.tar.gz && \
    tar zxvf dynamodb_local_${DYNAMODB_VERSION}.tar.gz && \
    rm dynamodb_local_${DYNAMODB_VERSION}.tar.gz


# ENTRYPOINT ["/usr/bin/java", "-Djava.library.path=.", "-jar", "DynamoDBLocal.jar", "-dbPath", "/var/dynamodb_local"]
ENTRYPOINT ["/usr/bin/java", "-Djava.library.path=.", "-jar", "DynamoDBLocal.jar", "-inMemory"]

EXPOSE 8000

CMD ["-port", "8000"]
