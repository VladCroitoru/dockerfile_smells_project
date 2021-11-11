FROM quay.io/powercloud/powervs-container-host:multi-arch

LABEL authors="Rafael Sene - rpsene@br.ibm.com"

WORKDIR /ocp-delete

RUN ibmcloud plugin update power-iaas --force

ENV API_KEY=""
ENV POWERVS_CRN=""
ENV CLUSTER_ID=""
ENV VPC_REGION=""

COPY ./delete.sh .

RUN chmod +x ./delete.sh

ENTRYPOINT ["/bin/bash", "-c", "./delete.sh"]
