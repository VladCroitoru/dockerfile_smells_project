FROM docker

ENV HOME /
# https://hub.docker.com/r/sbani/google-gloud-sdk/
RUN apk add --no-cache --virtual .build-deps \
		curl \
		bash \
	&& apk add --no-cache --virtual .cloudsdk-rundeps \
		openssh-client \
		python \
	&& curl -fSL https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.tar.gz -o google-cloud-sdk.tar.gz \
	&& tar -xzf google-cloud-sdk.tar.gz \
	&& google-cloud-sdk/install.sh \
		--usage-reporting=false \
		--path-update=true \
		--bash-completion=false \
		--rc-path=/.bashrc \
		--additional-components app kubectl alpha beta \
	\
	&& google-cloud-sdk/bin/gcloud config set --installation component_manager/disable_update_check true \
	&& sed -i -- 's/\"disable_updater\": false/\"disable_updater\": true/g' /google-cloud-sdk/lib/googlecloudsdk/core/config.json

ENV PATH /google-cloud-sdk/bin:$PATH
VOLUME ["/.config"]

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["/bin/bash"]
