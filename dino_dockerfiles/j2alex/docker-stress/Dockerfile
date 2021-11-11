FROM ubuntu

RUN apt-get update && apt-get install -y stress

ENTRYPOINT ["stress","--cpu","1","--vm","1","--vm-bytes","1024M","--vm-hang","0"]
