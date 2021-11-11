FROM lachlanevenson/k8s-kubectl:v1.5.1

RUN apk update && apk --no-cache add jq
ADD deploy.sh /deploy.sh
ENTRYPOINT ["/deploy.sh"]
