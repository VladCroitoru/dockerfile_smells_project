FROM ubuntu:xenial
MAINTAINER Gaurav Juvekar <gauravjuvekar@gmail.com>

# The last apt-get clean and rm -rf removes the temporary .deb packages
# downloaded during the install process
RUN apt-get update && \
	 apt-get install --no-install-recommends -y \
		aspell \
		aspell-en \
		poppler-utils \
		&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
