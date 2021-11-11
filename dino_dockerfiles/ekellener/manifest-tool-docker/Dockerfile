FROM ekellener/manifest-tool

RUN apt-get update && apt-get install vim -y

RUN  cd $GOPATH/src && \
mkdir -p github.com/estesp && \
cd github.com/estesp 

RUN  git clone https://github.com/estesp/manifest-tool .
RUN  make binary
COPY post_manifest.sh post_manifest.sh


ENTRYPOINT ["/bin/bash", "post_manifest.sh"]

