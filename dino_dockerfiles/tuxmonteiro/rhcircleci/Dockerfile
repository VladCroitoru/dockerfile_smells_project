FROM tuxmonteiro/docker-openjdk:8

MAINTAINER tuxmonteiro

RUN JQ_URL="https://circle-downloads.s3.amazonaws.com/circleci-images/cache/linux-amd64/jq-latest" \
    && curl --silent --show-error --location --fail --retry 3 --output /usr/bin/jq $JQ_URL \
    && chmod +x /usr/bin/jq \
    && jq --version \
    && groupadd --gid 3434 circleci \
    && useradd --uid 3434 --gid circleci --shell /bin/bash --create-home circleci \
    && yum install -y sudo \
    && yum clean all \
    && echo 'circleci ALL=NOPASSWD: ALL' >> /etc/sudoers.d/50-circleci

USER circleci

CMD ["/bin/sh"]
