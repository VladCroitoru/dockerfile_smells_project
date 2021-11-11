FROM apache/nifi-registry:0.1.0

ADD env2config.sh ${NIFI_REGISTRY_BASE_DIR}/scripts/
ADD run.sh ${NIFI_REGISTRY_BASE_DIR}/scripts/

CMD ${NIFI_REGISTRY_BASE_DIR}/scripts/run.sh
