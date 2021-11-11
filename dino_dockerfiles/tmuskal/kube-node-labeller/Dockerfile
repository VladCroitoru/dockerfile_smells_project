
FROM lachlanevenson/k8s-kubectl:latest

RUN apk --no-cache add bash py-pip python jq curl && \
    pip install --upgrade pip awscli
ENTRYPOINT ["/run.sh"]
ADD run.sh /run.sh

CMD /run.sh
