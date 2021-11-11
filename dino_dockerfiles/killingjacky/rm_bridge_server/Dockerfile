FROM softsam/android-19

MAINTAINER fuyaode

RUN apt-get update && \
    apt-get install -y openssh-server && \
    apt-get clean && \
    apt-get autoclean

EXPOSE 7474
COPY RMBridge_1.3.1.apk RMBridge_1.3.1.apk
COPY install.sh ./install.sh
RUN chmod +x ./install.sh
CMD ["./install.sh"]
