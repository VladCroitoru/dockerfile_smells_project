FROM heroku/cedar:14
MAINTAINER Jason Cox <jason.cox@panoply.fm>

# Install dependencies
RUN apt-get update -qq && apt-get install -y gcc build-essential libpq-dev python python-pip python-dev python-setuptools
RUN pip install -U crcmod
RUN pip install awscli

RUN \
 wget https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.zip -qO /tmp/google-cloud-sdk.zip && \
 unzip -qd /usr/local /tmp/google-cloud-sdk.zip && \
 /usr/local/google-cloud-sdk/install.sh --usage-reporting=false --path-update=false --bash-completion=false && \
 rm -rf /tmp/google-cloud-sdk.zip
ENV PATH /usr/local/google-cloud-sdk/bin:$PATH
RUN touch /etc/boto.cfg
RUN touch /etc/service_account_key.json
RUN mkdir /app
RUN addgroup --quiet --gid 2000 slug && \
    useradd slug --uid=2000 --gid=2000 --home-dir /app --no-create-home \
        --shell /bin/bash

WORKDIR /app

ADD ./runner /runner
RUN chmod +x /runner/init
RUN chown slug:slug /app /runner/init /etc/boto.cfg /etc/service_account_key.json

# make app binaries etc available
RUN echo '# source /app/.profile.d/* \n\
if [ -d /app/.profile.d ]; then \n\
  for i in /app/.profile.d/*.sh; do \n\
    if [ -r $i ]; then \n\
      echo $i \n\
      . $i \n\
    fi \n\
  done \n\
  unset i \n\
fi \n' >> /etc/profile

USER slug
ENV HOME /app

ENTRYPOINT ["/runner/init"]

ONBUILD RUN mkdir -p /app
ONBUILD WORKDIR /app
ONBUILD ADD slug.tgz /app
