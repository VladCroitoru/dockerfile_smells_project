FROM circleci/golang:1.9.0

RUN sudo apt-get install -y netcat \
                       python \
                       python-pip \
                       build-essential \
                       libpng-dev

RUN curl -o google-cloud-sdk-158.0.0-linux-x86_64.tar.gz https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-158.0.0-linux-x86_64.tar.gz
RUN tar xfv google-cloud-sdk-158.0.0-linux-x86_64.tar.gz
RUN ./google-cloud-sdk/install.sh
RUN ./google-cloud-sdk/bin/gcloud init
RUN gcloud components install app-engine-go

RUN go get -u github.com/golang/dep/cmd/dep
