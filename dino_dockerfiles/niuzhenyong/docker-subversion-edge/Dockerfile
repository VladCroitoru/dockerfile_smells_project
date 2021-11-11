FROM centos/systemd

LABEL maintainer Niu Zhenyong <niuzhenyong@qq.com>

ENV JAVA_HOME=/usr/java/default
ENV RUN_AS_USER=collabnet

RUN useradd collabnet && \
    cd /tmp && \
    curl -O -H "Cookie: oraclelicense=accept-securebackup-cookie" -H "Connection: keep-alive" -L "http://download.oracle.com/otn-pub/java/jdk/8u161-b12/2f38c3b165be4555a1fa6e98c45e0808/jre-8u161-linux-x64.rpm" && \
    yum install -y ./jre-8u161-linux-x64.rpm && \
    yum clean all && \
    rm ./jre-8u161-linux-x64.rpm && \
    curl -O -H "Connection: keep-alive" -L "https://downloads-guests.open.collab.net/files/documents/61/18759/CollabNetSubversionEdge-5.2.2_linux-x86_64.tar.gz" && \
    cd /opt && \
    tar zxf /tmp/CollabNetSubversionEdge-5.2.2_linux-x86_64.tar.gz && \
    rm /tmp/CollabNetSubversionEdge-5.2.2_linux-x86_64.tar.gz && \
    cp /opt/csvn/data/conf/csvn.conf.dist /opt/csvn/data/conf/csvn.conf && \
    sed -i "s/^USE_SYSTEMD=/USE_SYSTEMD=1/g" /opt/csvn/data/conf/csvn.conf && \
    sed -i "s/^RUN_AS_USER=/RUN_AS_USER=collabnet/g" /opt/csvn/data/conf/csvn.conf && \
    cd csvn && \
    ./bin/csvn install && \
    ./bin/csvn-httpd install && \
    cp -r ./data ./data_init && \
    chown -R collabnet.collabnet /opt/csvn && \
    echo "#!/bin/sh" > ~/init_data.sh && \
    echo "if [ ! -f /opt/csvn/data/conf/csvn.conf ]; then" >> ~/init_data.sh && \
    echo "    cp -a /opt/csvn/data_init/* /opt/csvn/data" >> ~/init_data.sh && \
    echo "    chown -R collabnet.collabnet /opt/csvn/data" >> ~/init_data.sh && \
    echo "fi" >> ~/init_data.sh && \
    chmod +x ~/init_data.sh && \
    echo "[Unit]" >> /etc/systemd/system/csvn-data-init.service && \
    echo "Description=CSVN Data Init" >> /etc/systemd/system/csvn-data-init.service && \
    echo "Before=csvn.service csvn-httpd.service" >> /etc/systemd/system/csvn-data-init.service && \
    echo "" >> /etc/systemd/system/csvn-data-init.service && \
    echo "[Service]" >> /etc/systemd/system/csvn-data-init.service && \
    echo "Type=oneshot" >> /etc/systemd/system/csvn-data-init.service && \
    echo "ExecStart=/root/init_data.sh" >> /etc/systemd/system/csvn-data-init.service && \
    echo "" >> /etc/systemd/system/csvn-data-init.service && \
    echo "[Install]" >> /etc/systemd/system/csvn-data-init.service && \
    echo "WantedBy=multi-user.target" >> /etc/systemd/system/csvn-data-init.service && \
    systemctl enable csvn-data-init.service
    
EXPOSE 3343 4434 18080

VOLUME /opt/csvn/data

WORKDIR /opt/csvn

CMD [ "/usr/sbin/init" ]
