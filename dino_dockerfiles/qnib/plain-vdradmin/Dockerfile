FROM qnib/dplain-init

ENV SVDRP_PORT=6419 \
    VDRADMIN_PORT=8001 \
    ENTRYPOINTS_DIR=/opt/qnib/entry
RUN apt-get update \
 && apt-get install -y vdradmin-am
COPY etc/vdradmind.conf /etc/vdradmin-am/
COPY opt/qnib/entry/10-vdradmin.sh /opt/qnib/entry/
CMD ["vdradmind", "--nofork", "-l", "7", "-d", "/etc/vdradmin-am/"]
