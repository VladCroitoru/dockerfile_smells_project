FROM google/cloud-sdk
RUN apt-get update && apt-get --no-install-recommends -y install \
		jq \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /opt

COPY gke-auto-snapshot.sh .

ENTRYPOINT ["./gke-auto-snapshot.sh"]
