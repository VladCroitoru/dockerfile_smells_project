FROM openjdk

RUN apt-get update && \
    apt-get upgrade -y awscli

WORKDIR /home/docker
ENV DATADIR=/var/lib/dynamo
ENV AWS_ACCESS_KEY_ID=dummy
ENV AWS_SECRET_ACCESS_KEY=dummy
ENV AWS_DEFAULT_REGION=eu-west-1

RUN /usr/bin/curl -L https://s3.eu-central-1.amazonaws.com/dynamodb-local-frankfurt/dynamodb_local_latest.tar.gz | /bin/tar xz

EXPOSE 6060
VOLUME $DATADIR

COPY entrypoint.sh /root/entrypoint.sh
COPY create_tables/submitted_responses.sh /root/create_tables/submitted_responses.sh
COPY create_tables/questionnaire_state.sh /root/create_tables/questionnaire_state.sh
COPY create_tables/eq_session.sh /root/create_tables/eq_session.sh
COPY create_tables/used_jti_claim.sh /root/create_tables/used_jti_claim.sh

# Configure a sane default Java heap size (that can be overridden).
ENV JAVA_OPTS "-Xmx256m"

ENTRYPOINT ["/root/entrypoint.sh", "-dbPath /var/lib/dynamo"]