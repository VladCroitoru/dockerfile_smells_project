FROM python:2.7-alpine
ENV PATH /google-cloud-sdk/bin:$PATH
RUN apk update && apk add jq wget bash && rm -rf /var/cache/apk/* && \
    wget https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz --no-check-certificate && \
    tar zxvf google-cloud-sdk.tar.gz && \
    rm google-cloud-sdk.tar.gz && \
    ./google-cloud-sdk/install.sh --usage-reporting=true --path-update=true && \
    gcloud --quiet components update && \
    gcloud --quiet components install kubectl

ADD gcloud_auth.sh .
RUN chmod +x gcloud_auth.sh
ENTRYPOINT ["./gcloud_auth.sh"]
