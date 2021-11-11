FROM deis/registry

ENV SETTINGS_FLAVOR s3
ENV AWS_BUCKET XXXXXXXXXXXXXXX
ENV STORAGE_PATH /XXXXXXXXXXXXXXX
ENV AWS_KEY XXXXXXXXXXXXXXX
ENV AWS_SECRET XXXXXXXXXXXXXXX
ENV SEARCH_BACKEND XXXXXXXXXXXXXXX
ENV AWS_REGION ceph
ENV AWS_HOST XXXXXXXXXXXXXXX
ENV AWS_SECURE false
ENV AWS_ENCRYPT false
ENV DOCKER_REGISTRY_CONFIG /docker-registry/config/config_sample.yml

ADD https://raw.githubusercontent.com/lorieri/docker-registry/d923eda8836881e58f0908771ef502d295eb4536/docker_registry/drivers/s3.py /usr/local/lib/python2.7/dist-packages/docker_registry/drivers/s3.py

ADD https://raw.githubusercontent.com/lorieri/docker-registry/0441df74e47e613be51683567ec2700a5ee0edce/config/config_sample.yml /docker-registry/config/config_sample.yml

WORKDIR /app
CMD ["/app/bin/boot"]
EXPOSE 5000
