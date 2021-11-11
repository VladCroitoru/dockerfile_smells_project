FROM debian:latest 

ENV VOLUME_TAG="rexray" \
    AWS_ACCESS_KEY_ID="AWS_ACCESS_KEY_ID not set." \
    AWS_SECRET_ACCESS_KEY="AWS_SECRET_ACCESS_KEY not set." \
    AWS_SECURITY_GROUP_ID="AWS_SECURITY_GROUP_ID not set." \
    AWS_REGION="AWS_REGION not set."

RUN apt-get update && \
    apt-get install -y curl nfs-common && \
    apt-get clean && \
    curl -sSL https://dl.bintray.com/emccode/rexray/install | sh -s -- stable 0.6.4

COPY entrypoint.sh /entrypoint.sh

CMD /entrypoint.sh
