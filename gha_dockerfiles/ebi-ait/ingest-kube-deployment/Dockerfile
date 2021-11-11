FROM alpine:3.10.2

ARG user=ingest
ARG repo=https://github.com/ebi-ait/ingest-kube-deployment.git

# install base packages	and add	user
RUN apk add --no-cache \
      bash \
      shadow \
      curl \
      ncurses \
      python3 \
      python3-dev	\
      git	\
      jq \
      make \
      openssh \
    && pip3 install --upgrade pip \
    && cd /usr/bin \
    && ln -sf python3 python \
    && ln -sf pip3 pip \
    && pip install awscli \
    && useradd -ms /bin/bash $user

USER $user
WORKDIR /home/$user

RUN mkdir /home/$user/opt
ENV PATH=/home/$user/opt:$PATH

# install additional tools needed for ingest deployment
RUN cd opt \
    && curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.16.10/bin/linux/amd64/kubectl \
    && wget https://raw.githubusercontent.com/ahmetb/kubectx/master/kubectx \
    && wget https://raw.githubusercontent.com/ahmetb/kubectx/master/kubens \
    && chmod +x kubectl kubectx kubens \
    && wget https://get.helm.sh/helm-v2.16.1-linux-amd64.tar.gz \
    && tar -zxvf helm-v2.16.1-linux-amd64.tar.gz \
    && mv linux-amd64/* . && rm -rf linux-amd64/ \
    && wget https://releases.hashicorp.com/terraform/0.12.25/terraform_0.12.25_linux_amd64.zip \
    && unzip terraform_0.12.25_linux_amd64.zip \
    && wget https://amazon-eks.s3-us-west-2.amazonaws.com/1.14.6/2019-08-22/bin/linux/amd64/aws-iam-authenticator \
    && chmod +x aws-iam-authenticator \
    && ln -s aws-iam-authenticator heptio-authenticator-aws

RUN mkdir -p .aws .kube

# make sure these 2 files are in current dir
COPY config .aws
COPY credentials .aws

RUN git clone $repo

#RUN ["/bin/bash", "-c", "cd ingest-kube-deployment && source config/environment_dev && cd infra && make retrieve-kubeconfig-dev"]

# build - replace name tag below
#docker build --no-cache -t prabht/ingest-env .

# run
#docker run -it prabht/ingest-env:latest /bin/bash