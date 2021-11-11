FROM crosbymichael/python

MAINTAINER Ross Kukulinski <ross@kukulinski.com>

RUN pip install rethinkdb

ENV LC_ALL C.UTF-8

# Prepare the image.
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y -qq --no-install-recommends wget unzip python php5-mysql php5-cli php5-cgi openjdk-7-jre-headless openssh-client python-openssl && apt-get clean

# Install the Google Cloud SDK.
ENV HOME /
ENV CLOUDSDK_PYTHON_SITEPACKAGES 1
RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip && unzip google-cloud-sdk.zip && rm google-cloud-sdk.zip
RUN google-cloud-sdk/install.sh --usage-reporting=true --path-update=true --bash-completion=true --rc-path=/.bashrc --additional-components app-engine-java app-engine-python app kubectl alpha beta gcd-emulator pubsub-emulator cloud-datastore-emulator app-engine-go bigtable


# Disable updater check for the whole installation.
# Users won't be bugged with notifications to update to the latest version of gcloud.
RUN google-cloud-sdk/bin/gcloud config set --installation component_manager/disable_update_check true

# Disable updater completely.
# Running `gcloud components update` doesn't really do anything in a union FS.
# Changes are lost on a subsequent run.
RUN sed -i -- 's/\"disable_updater\": false/\"disable_updater\": true/g' /google-cloud-sdk/lib/googlecloudsdk/core/config.json

ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 /usr/local/bin/dumb-init
RUN chmod +x /usr/local/bin/dumb-init
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]

RUN mkdir /.ssh
ENV PATH /google-cloud-sdk/bin:$PATH

ADD backup.sh backup.sh
ADD restore.sh restore.sh
ADD drop-dbs.py drop-dbs.py

CMD "/backup.sh"
