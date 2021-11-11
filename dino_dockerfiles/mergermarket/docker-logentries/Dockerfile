FROM logentries/docker-logentries
RUN apt-get update && apt-get install -y patch
ADD ignore.patch ignore.patch
RUN patch -p0 < ignore.patch
