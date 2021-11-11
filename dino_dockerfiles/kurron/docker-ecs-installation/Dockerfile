FROM python:latest

MAINTAINER Ron Kurr <kurr@kurron.org>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get --quiet update && \
    apt-get --quiet --yes install groff less && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip python-dateutil awscli

ADD install-definitions.sh /install-definitions.sh

# Set the AWS environment variables
ENV AWS_ACCESS_KEY_ID OVERRIDE ME 
ENV AWS_SECRET_ACCESS_KEY OVERRIDE_ME
ENV AWS_REGION OVERRIDE_ME 

# Set the Artifactory variables 
ENV BRANCH=OVERRIDE_ME
ENV MAJOR=OVERRIDE_ME
ENV MINOR=OVERRIDE_ME
ENV PATCH=OVERRIDE_ME
ENV GROUP=OVERRIDE_ME
ENV RELEASE_URL=OVERRIDE_ME
ENV MILESTONE_URL=OVERRIDE_ME
ENV ARTIFACT_ID=OVERRIDE_ME

WORKDIR /tmp

ENTRYPOINT ["/install-definitions.sh"]
