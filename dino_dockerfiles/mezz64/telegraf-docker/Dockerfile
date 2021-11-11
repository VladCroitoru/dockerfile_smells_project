FROM telegraf:latest

MAINTAINER mezz64 <jtmihalic@gmail.com>

RUN apt-get update && \
    apt-get install -yq \
    ipmitool && \
# Cleanup
    apt-get clean && \
    rm -rf \
	/tmp/* \
	/var/lib/apt/lists/* \
	/var/tmp/*

# CMD ["telegraf"]
