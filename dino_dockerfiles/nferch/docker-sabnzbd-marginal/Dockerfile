FROM linuxserver/sabnzbd

COPY ca.crt /usr/local/share/ca-certificates
COPY newca.crt /usr/local/share/ca-certificates
COPY 99-hostname-hack /etc/cont-init.d/
RUN update-ca-certificates
