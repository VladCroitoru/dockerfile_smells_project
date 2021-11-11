FROM docker:1.12
RUN apk --update add tar curl bash grep && \
  curl -Lsk https://github.com/kubernetes-incubator/bootkube/releases/download/v0.3.1/bootkube.tar.gz | tar zxv && \
  rm -rf /bin/darwin /bin/linux/checkpoint

ENV PATH=$PATH:/bin/linux

ADD manifests /manifests
ADD tar_asset.sh /tar_asset.sh
ADD retag.sh /retag.sh
ADD list-images.sh /list-images.sh
#ENTRYPOINT ["/entrypoint.sh"]
VOLUME ["/out"]
ENV BOOTKUBE_API_SERVERS=https://127.0.0.1:443 
ENV BOOTKUBE_ETCD_SERVERS=http://127.0.0.1:2379
#ENV TAG_PREFIX=127.0.0.1:5000/prod
