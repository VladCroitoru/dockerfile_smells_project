FROM qnib/uplain-init

ENV VDR_VNSI_PORT=34890 \
    SVDRP_PORT=6419 \
    VDR_SATIP_DEVICE=192.168.1.38|DVBS2-2:S19.2E
RUN apt-get update 
RUN apt-get install -y vdr-plugin-satip 
RUN apt-get install -y vdr-plugin-vnsiserver
RUN apt-get install -y vdr-plugin-epgsearch
ENV TZ=Europe/Berlin
RUN apt-get install -y tzdata
COPY etc/channels.conf etc/setup.conf /var/lib/vdr/
COPY etc/allowed_hosts.conf /var/lib/vdr/plugins/vnsiserver/allowed_hosts.conf
COPY bin/start.sh /opt/qnib/vdr/bin/
VOLUME ["/var/lib/video"]
CMD ["/opt/qnib/vdr/bin/start.sh"]
