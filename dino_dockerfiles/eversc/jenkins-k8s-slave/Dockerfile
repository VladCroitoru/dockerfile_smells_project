FROM gcr.io/cloud-solutions-images/jenkins-k8s-slave:v3

LABEL maintainer="eversmcc@gmail.com"

RUN apt-get clean && \
    apt-get update && \
    apt-get install -y \
        libeclipse-aether-java=1.0.2-1~bpo8+1 \
        libguice-java=4.0-2~bpo8+1 \
        libmaven3-core-java=3.3.9-3~bpo8+1 \
        libsisu-inject-java=0.3.2-1~bpo8+1 \
        libsisu-plexus-java=0.3.2-1~bpo8+1 \
        maven=3.3.9-3~bpo8+1 &&\
    apt-get clean