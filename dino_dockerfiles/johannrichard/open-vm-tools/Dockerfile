FROM debian:jessie

RUN apt-get update && \
	apt-get install -y --no-install-recommends open-vm-tools && \
	rm -rf /var/lib/apt/lists/*

CMD ["/usr/bin/vmtoolsd"]