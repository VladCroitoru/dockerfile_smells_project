FROM dorowu/ubuntu-desktop-lxde-vnc

ADD https://global.download.synology.com/download/Tools/SynologyCloudSyncDecryptionTool/013/Linux/x86_64/SynologyCloudSyncDecryptionTool-013_x64.tar.gz /app/
ADD ./decryptor.desktop /usr/share/applications/

WORKDIR /app

RUN cd /app/ && tar zxvf /app/SynologyCloudSyncDecryptionTool-013_x64.tar.gz
