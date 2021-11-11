FROM gianebao/bitbucket-pipeline-go-mysql

ENV TZ Asia/Singapore

ENV APP_PORT 443
ENV APP_REF_DOCS http://0.0.0.0:8081
ENV APP_ACCESS_LOG /log/access.log
ENV APP_ENV TESTING
ENV APP_NAME myapp
ENV REPO_OWNER github.com/someone

RUN \
 apt-get update && apt-get -y upgrade &&\
 apt-get -y install unzip groff

RUN \
 curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" &&\
 unzip awscli-bundle.zip &&\
 ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws &&\
 rm -rfv awscli-bundle awscli-bundle.zip

RUN \
 curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest &&\
 chmod 755 /usr/local/bin/ecs-cli

ADD scripts /scripts
RUN chmod -R 755 /scripts
ENV PATH $PATH:/scripts
