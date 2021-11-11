FROM            harbor-core.k8s-2.livelace.ru/dev/jvm:latest

ARG             OPENNLP_VERSION
ARG             MODEL_GENERATION

ENV             SOURCE_PATH="data/opennlp/model/${OPENNLP_VERSION}/${MODEL_GENERATION}/news/ru"
ENV             DESTINATION_PATH="/models/news/ru"

USER            root

RUN             mkdir -p "${DESTINATION_PATH}"

COPY            "${SOURCE_PATH}/all.bin"       "${DESTINATION_PATH}/all.bin"
COPY            "${SOURCE_PATH}/date.bin"      "${DESTINATION_PATH}/date.bin"
COPY            "${SOURCE_PATH}/event.bin"     "${DESTINATION_PATH}/event.bin"
COPY            "${SOURCE_PATH}/fac.bin"       "${DESTINATION_PATH}/fac.bin"
COPY            "${SOURCE_PATH}/gpe.bin"       "${DESTINATION_PATH}/gpe.bin"
COPY            "${SOURCE_PATH}/loc.bin"       "${DESTINATION_PATH}/loc.bin"
COPY            "${SOURCE_PATH}/money.bin"     "${DESTINATION_PATH}/money.bin"
COPY            "${SOURCE_PATH}/org.bin"       "${DESTINATION_PATH}/org.bin"
COPY            "${SOURCE_PATH}/per.bin"       "${DESTINATION_PATH}/per.bin"
COPY            "${SOURCE_PATH}/time.bin"      "${DESTINATION_PATH}/time.bin"
COPY            "${SOURCE_PATH}/sentence.bin"  "${DESTINATION_PATH}/sentence.bin"

COPY            "${SOURCE_PATH}/all.stat"      "${DESTINATION_PATH}/all.stat"
COPY            "${SOURCE_PATH}/date.stat"     "${DESTINATION_PATH}/date.stat"
COPY            "${SOURCE_PATH}/event.stat"    "${DESTINATION_PATH}/event.stat"
COPY            "${SOURCE_PATH}/fac.stat"      "${DESTINATION_PATH}/fac.stat"
COPY            "${SOURCE_PATH}/gpe.stat"      "${DESTINATION_PATH}/gpe.stat"
COPY            "${SOURCE_PATH}/loc.stat"      "${DESTINATION_PATH}/loc.stat"
COPY            "${SOURCE_PATH}/money.stat"    "${DESTINATION_PATH}/money.stat"
COPY            "${SOURCE_PATH}/org.stat"      "${DESTINATION_PATH}/org.stat"
COPY            "${SOURCE_PATH}/per.stat"      "${DESTINATION_PATH}/per.stat"
COPY            "${SOURCE_PATH}/time.stat"     "${DESTINATION_PATH}/time.stat"
COPY            "${SOURCE_PATH}/sentence.stat" "${DESTINATION_PATH}/sentence.stat"

COPY            "work/target/digator-opennlp-1.0-SNAPSHOT-runner.jar" "/digator-opennlp.jar"

USER            user

CMD             ["java", "-jar", "/digator-opennlp.jar"]
