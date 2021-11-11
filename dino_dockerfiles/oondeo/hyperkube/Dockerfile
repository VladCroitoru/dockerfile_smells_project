FROM gcr.io/google_containers/hyperkube-amd64:v1.3.7
ENV K8S_VERSION=v1.3.7 CALICOCNI_VERSION=v1.4.2 CNI_VERSION=v0.3.0 CALICO_VERSION=v0.22.0

RUN apt-get update && apt-get install -y conntrack vim-nox && rm -rf /var/lib/apt

RUN mkdir -p /opt/cni/bin \
  && curl -L https://github.com/appc/cni/releases/download/$CNI_VERSION/cni-$CNI_VERSION.tgz | tar zxv -C /opt/cni/bin \
  && chmod +x /opt/cni/bin/*
  
RUN curl -L https://github.com/projectcalico/calico-cni/releases/download/$CALICOCNI_VERSION/calico -o /opt/cni/bin/calico \
  && curl -L https://github.com/projectcalico/calico-cni/releases/download/$CALICOCNI_VERSION/calico-ipam -o /opt/cni/bin/calico-ipam \
  && chmod +x /opt/cni/bin/calico*

RUN curl -L http://storage.googleapis.com/kubernetes-release/release/${K8S_VERSION}/bin/linux/amd64/kubectl -o /usr/bin/kubectl \
  && chmod +x /usr/bin/kubectl

RUN curl -L https://github.com/projectcalico/calico-containers/releases/download/${CALICO_VERSION}/calicoctl -o /usr/bin/calicoctl \
 && chmod +x /usr/bin/calicoctl

#RUN curl -L https://raw.githubusercontent.com/kubernetes/kubernetes/master/cluster/images/hyperkube/copy-addons.sh -o /copy-addons.sh \
# && chmod +x /copy-addons.sh
