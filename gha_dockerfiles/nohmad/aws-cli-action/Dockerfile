FROM amazon/aws-cli
RUN yum install -y jq
RUN mkdir -p /root/.aws
WORKDIR /aws
ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
