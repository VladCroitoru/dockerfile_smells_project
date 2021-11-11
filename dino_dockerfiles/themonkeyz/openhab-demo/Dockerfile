FROM java:openjdk-7-jre

RUN mkdir /app &&\
    cd /app &&\
    wget https://bintray.com/artifact/download/openhab/bin/distribution-1.8.3-runtime.zip &&\
    unzip distribution-1.8.3-runtime.zip &&\
    rm distribution-1.8.3-runtime.zip &&\
    wget https://bintray.com/artifact/download/openhab/bin/distribution-1.8.3-demo.zip &&\
    unzip -o distribution-1.8.3-demo.zip &&\
    rm distribution-1.8.3-demo.zip &&\
    mv configurations/openhab_default.cfg configurations/openhab.cfg

EXPOSE 8080

CMD cd /app && ./start.sh

