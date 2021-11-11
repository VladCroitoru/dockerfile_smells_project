FROM google/cloud-sdk

RUN apt-get install -y curl
# TODO: version shoud be added from docker command
# version 1.6.2 is for coreos alpha version
RUN curl -s https://get.docker.com/builds/Linux/x86_64/docker-1.6.2 -o docker
RUN chmod +x docker
RUN cp docker /usr/bin/

RUN gcloud components update -q && \
    gcloud components update -q alpha && \
    gcloud components update -q beta && \
    gcloud components update -q preview
