FROM jpizarrom/beaglebone-kura:1.4.0-20160704

RUN [ "cross-build-start" ]

## Variable ENV
ENV ZB_FOLDER=/opt/zb

RUN mkdir -p ${ZB_FOLDER}

## Add file
ADD ./start_kura_zb.sh ${ZB_FOLDER}/
ADD ./bundles/sensor.dp /opt/eclipse/kura/kura/packages/
ADD ./bundles/zigbee4java.dp /opt/eclipse/kura/kura/packages/
ADD ./bundles/publisher.dp /opt/eclipse/kura/kura/packages/

ADD ./bundles/dpa.properties /opt/eclipse/kura/kura/dpa.properties

## Custom Kura installation
RUN chmod 755 ${ZB_FOLDER}/*.sh

## Main start
CMD ${ZB_FOLDER}/start_kura_zb.sh

RUN [ "cross-build-end" ]
