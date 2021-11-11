FROM google/cloud-sdk:alpine
RUN apk add --no-cache curl ca-certificates coreutils
ADD gcloud-snapshot.sh /gcloud-snapshot.sh
ENTRYPOINT /gcloud-snapshot.sh -p $PROJECT_ID -d ${OLDER_THAN:-7}
