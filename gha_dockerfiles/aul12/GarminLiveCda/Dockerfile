FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y wget unzip vim make openssl screen && \
    apt-get install -y libcurl4 libexpat1 libglib2.0-0 libxext6 libxxf86vm1 libsm6 libgtk2.0-0 libwebkitgtk-1.0-0 default-jre

COPY post_install.sh /post_install.sh
COPY entrypoint.sh /entrypoint.sh
RUN wget -nv -O sdk-manager.zip https://developer.garmin.com/downloads/connect-iq/sdk-manager/connectiq-sdk-manager-linux.zip &&\
    unzip -d /sdk-manager sdk-manager.zip && \
    rm sdk-manager.zip && \
    chmod +x /post_install.sh && \
    chmod +x /entrypoint.sh


RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    chown ${uid}:${gid} -R /home/developer
USER developer
ENV DISPLAY=:0

WORKDIR /home/developer
CMD ["/bin/bash"]


