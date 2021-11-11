FROM ghellings/docker-aws-cli
RUN apk add --no-cache jq curl && \
    apk upgrade python py-pip && \
    pip install --upgrade awscli &&\
    pip install docker-cloud
ADD ./script.sh /

ENV SERVICE="" \
    STACK="" \
    PORT="" \
    REGION="us-west-1" \ 
    ARN=""



CMD ./script.sh
