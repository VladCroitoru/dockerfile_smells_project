FROM debian:jessie

MAINTAINER Samuel Terburg

ENV  FILTER   ""
ENV  TEMPLATE "/templates/proxy.tpl"

COPY watch.sh   /watch.sh
COPY templates/ /templates/
COPY oc         /usr/bin/kubectl

#RUN curl -sSL https://github.com/openshift/origin/releases/download/v1.3.0/openshift-origin-client-tools-v1.3.0-3ab7af3d097b57f933eccef684a714f2368804e7-linux-64bit.tar.gz |tar -C /usr/local/bin/ -xzv --strip-components=1 */oc

#ADD https://github.com/openshift/origin/releases/download/v1.3.0/openshift-origin-client-tools-v1.3.0-3ab7af3d097b57f933eccef684a714f2368804e7-linux-64bit.tar.gz /tmp/oc.tar.gz
#RUN tar -C /usr/bin/ -xzvf /tmp/oc.tar.gz --wildcards --strip-components=1 openshift-origin-client-tools*/oc && rm /tmp/oc.tar.gz

CMD /watch.sh

