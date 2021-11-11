FROM python

MAINTAINER Allen Vailliencourt <allen.vailliencourt@forty8fiftylabs.com>

RUN apt-get update && apt-get upgrade -y && \
    git clone https://github.com/Alfresco/aws-cis-security-benchmark && \
    pip install awscli ansi2html
# Adding a non-root user
RUN groupadd -r prowler && useradd -ms /bin/bash -r -g prowler prowler && \
    chown -R prowler:prowler /aws-cis-security-benchmark

ENV AWS_PROFILE="default" \
    AWS_REGION="us-east-1"
        
COPY prowler-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Runs application as prowler and not root
USER prowler
WORKDIR /reports

ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
