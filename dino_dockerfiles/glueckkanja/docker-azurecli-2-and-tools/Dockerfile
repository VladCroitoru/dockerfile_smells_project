FROM azuresdk/azure-cli-python

# samba
RUN apk update && apk add cifs-utils rsync zip jq less

# git lfs
RUN apk --no-cache add openssl git curl \
  && curl -sLO https://github.com/git-lfs/git-lfs/releases/download/v2.3.0/git-lfs-linux-amd64-2.3.0.tar.gz \
  && tar zxvf git-lfs-linux-amd64-2.3.0.tar.gz \
  && mv git-lfs-2.3.0/git-lfs /usr/bin/ \
  && rm -rf git-lfs-2.3.0 \
  && rm -rf git-lfs-linux-amd64-2.3.0.tar.gz
  
