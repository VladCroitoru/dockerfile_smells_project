# syntax=docker/dockerfile:1
FROM amazon/aws-cli:latest

RUN yum install git jq tar rsync -y && \
    amazon-linux-extras install docker && \
    useradd -u 1000 -d /home/tools tools && \
    usermod -aG docker tools

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod u+x /entrypoint.sh

WORKDIR /home/tools

COPY init.sh .
COPY clean-up.sh .
COPY docker/bashrc.sh .bashrc
COPY release.sh .
COPY create-bucket.sh .
COPY push.sh .
COPY secrets_scan.sh .
COPY common/IaC/ .

RUN chown -R tools /home/tools && \
    chmod -R u+x /home/tools/*.sh

ENTRYPOINT ["/entrypoint.sh"]

USER tools
CMD ["--mode", "repl"]
