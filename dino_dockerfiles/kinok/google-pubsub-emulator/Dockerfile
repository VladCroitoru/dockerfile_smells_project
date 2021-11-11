FROM java:8-jre

MAINTAINER Michael INTHILITH <minthilith@gmail.com> 
LABEL version="1.0.1"
LABEL app="pubsub-emulator"

ENV CLOUDSDK_CORE_DISABLE_PROMPTS 1
ENV DATA_DIR "/data"
ENV HOST_PORT 8042

RUN apt-get update && \
	apt-get install -yqq curl \
		python && \
	apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

RUN \
	curl https://sdk.cloud.google.com | bash && \
 	cat /root/google-cloud-sdk/path.bash.inc | bash && \
 	cat /root/google-cloud-sdk/completion.bash.inc | bash && \
 	/root/google-cloud-sdk/bin/gcloud components install -q pubsub-emulator beta

COPY start.sh /start.sh

RUN chmod +x /start.sh

CMD ["/start.sh"]

EXPOSE 8042
