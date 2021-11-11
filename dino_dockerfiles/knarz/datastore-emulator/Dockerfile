FROM java:jre-alpine

MAINTAINER Sascha Hanse <shanse@gmail.com>
LABEL app="datastore-emulator"

ENV IN_MEMORY "false"
ENV CLOUDSDK_CORE_DISABLE_PROMPTS 1
ENV DATA_DIR "/opt/datastore"
ENV HOST_PORT 8432
ENV CONSISTENCY 0.9
ENV CLOUDSDK_CORE_PROJECT "test-project"

RUN apk add --no-cache curl bash python

RUN curl https://sdk.cloud.google.com | bash && \
			/root/google-cloud-sdk/bin/gcloud config set disable_usage_reporting true && \
			/root/google-cloud-sdk/bin/gcloud components install -q cloud-datastore-emulator beta

RUN mkdir -p ${DATA_DIR}
EXPOSE 8432

ADD start_datastore_emu.sh /opt
RUN chmod +x /opt/start_datastore_emu.sh

CMD ["/opt/start_datastore_emu.sh"]
