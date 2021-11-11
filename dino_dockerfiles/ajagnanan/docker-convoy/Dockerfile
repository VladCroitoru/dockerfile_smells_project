FROM ubuntu
RUN apt-get update && apt-get install -y openssl wget
RUN wget https://github.com/rancher/convoy/releases/download/v0.4.3/convoy.tar.gz && tar xvf convoy.tar.gz && cp convoy/convoy convoy/convoy-pdata_tools /usr/local/bin/ && rm convoy.tar.gz
ADD run.sh .
ENTRYPOINT [ "bash","run.sh" ]
