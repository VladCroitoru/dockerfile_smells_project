FROM drupal:8.3

# https://www.drupal.org/project/lightning/releases/8.x-2.13
ENV LIGHTNING_VERSION 8.x-2.13
ENV LIGHTNING_MD5 2921361da11004bd06914aae36884f58

RUN curl -fSL "https://ftp.drupal.org/files/projects/lightning-${LIGHTNING_VERSION}-no-core.tar.gz" -o lightning.tar.gz \
	&& echo "${LIGHTNING_MD5} *lightning.tar.gz" | md5sum -c - \
	&& tar -xzf lightning.tar.gz -C profiles/ \
	&& rm lightning.tar.gz \
