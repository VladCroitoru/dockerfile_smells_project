FROM registry.access.redhat.com/ubi7/ubi

RUN yum install -y git
RUN curl -sL https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/linux/oc.tar.gz -o ${HOME}/oc.tar.gz && \
    cd ${HOME} && \
    tar -xvzf oc.tar.gz && \
    chmod +x oc && \
    mkdir -p $HOME/bin && \
    mv ./oc /usr/bin/oc && \
    PATH=$HOME/bin:$PATH && \
    oc version && \
    curl -sL https://github.com/argoproj/argo-workflows/releases/download/v2.11.0/argo-linux-amd64.gz -o argo-linux.gz && \
    gunzip argo-linux.gz && \
    chmod +x argo-linux && \
    mv ./argo-linux /usr/bin/argo && \
    argo version
COPY ./loopscript.sh $HOME/loopscript.sh


WORKDIR $HOME

ENTRYPOINT ["bash", "loopscript.sh"]
