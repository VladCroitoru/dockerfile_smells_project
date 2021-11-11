FROM google/cloud-sdk:alpine
RUN apk --update add openjdk8-jre && rm -rf /tmp/*
RUN gcloud components install beta cloud-datastore-emulator -q && rm -rf /google-cloud-sdk/.install/.backup
