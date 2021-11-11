FROM debian:stretch-slim

ARG USER_ID
ARG GROUP_ID

ENV ZCASH_VERSION 4.5.1+1
ENV HOME /home/zcash

# add user with specified (or default) user/group ids
ENV USER_ID ${USER_ID:-1000}
ENV GROUP_ID ${GROUP_ID:-1000}

RUN groupadd -g ${GROUP_ID} zcash \
	&& useradd -u ${USER_ID} -g zcash -s /bin/bash -m -d ${HOME} zcash

RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y --no-install-recommends apt-transport-https gnupg ca-certificates wget gosu && \
  wget -qO - https://apt.z.cash/zcash.asc | apt-key add - && \
  echo "deb https://apt.z.cash/ stretch main" | tee /etc/apt/sources.list.d/zcash.list && \
  apt-get update && \
  apt-get install -y --no-install-recommends zcash=$ZCASH_VERSION && \
  apt-get purge -y apt-transport-https && \
  apt-get autoclean

#RUN zcash-fetch-params

COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["zcashd"]
