FROM iganarix/cld-gcloud

ARG _ver='0.12.18'
RUN curl https://releases.hashicorp.com/terraform/${_ver}/terraform_${_ver}_linux_amd64.zip -o /usr/local/bin/terraform_${_ver}_linux_amd64.zip && \
    cd /usr/local/bin/ && \
    unzip terraform_${_ver}_linux_amd64.zip && \
    rm -f /usr/local/bin/terraform_${_ver}_linux_amd64.zip

RUN gcloud --quiet components update && \
    gcloud --quiet components install beta