FROM ubuntu:18.04
RUN rm -f /etc/apt/apt.conf.d/01autoremove-kernels \
 \
 && echo 'DPkg::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' > /etc/apt/apt.conf.d/docker-clean \
 && echo 'APT::Update::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' >> /etc/apt/apt.conf.d/docker-clean \
 && echo 'Dir::Cache::pkgcache "";' >> /etc/apt/apt.conf.d/docker-clean \
 && echo 'Dir::Cache::srcpkgcache "";' >> /etc/apt/apt.conf.d/docker-clean \
 \
 && echo 'Acquire::Languages "none";' > /etc/apt/apt.conf.d/docker-no-languages \
 \
 && echo 'Acquire::GzipIndexes "true";' > /etc/apt/apt.conf.d/docker-gzip-indexes \
 && echo 'Acquire::CompressionTypes::Order:: "gz";' > /etc/apt/apt.conf.d/docker-gzip-indexes \
 \
 && echo 'Apt::AutoRemove::SuggestsImportant "false";' > /etc/apt/apt.conf.d/docker-autoremove-suggests

RUN apt-get update && apt-get dist-upgrade -y && apt-get install -y git make curl wget apache2 dumb-init && rm -rf /var/lib/apt /var/cache/apt

VOLUME /root/.ipfs
VOLUME /var/log/apache2

ENTRYPOINT ["/usr/bin/dumb-init", "/app/run.sh"]
EXPOSE 80

HEALTHCHECK --interval=30s  --timeout=10s --retries=3 CMD curl -f http://localhost

#IPFS
RUN git clone https://github.com/mkg20001/dist.ipfs.io-installer ipfsio && \
  make -C ipfsio install && \
  ipfs-installer update-cache && \
  ipfs-installer install go-ipfs && \
  ipfs-installer install fs-repo-migrations && \
  rm -rf ipfsio

RUN rm /etc/apache2/mods-available/proxy_http2.load && a2enmod expires rewrite headers proxy*

COPY apache.conf /etc/apache2/sites-available/000-default.conf

COPY app /app
WORKDIR /app
