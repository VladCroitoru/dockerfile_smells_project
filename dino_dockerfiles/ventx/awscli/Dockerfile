FROM ventx/alpine:3.6

ENV AWSCLI 1.16.96

RUN  apk --update add git openssh-client python py-pip && \
  pip install --upgrade pip && \
  pip install awscli==${AWSCLI}  
  
WORKDIR /work

ENTRYPOINT ["aws"]
