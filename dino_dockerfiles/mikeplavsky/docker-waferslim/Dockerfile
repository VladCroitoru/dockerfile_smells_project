FROM python:3.5.2

RUN mkdir binaries && \
    cd /binaries && \
    curl -o fitnesse-standalone.jar -L \
    "http://fitnesse.org/fitnesse-standalone.jar?responder=releaseDownload&release=20160618" && \
    apt-get update && \
    apt-get install -qq -y unzip openjdk-7-jre-headless jq && \
    chmod 777 /binaries/fitnesse-standalone.jar

ENV W_URL https://pypi.python.org/packages/65/60/d154ad7ebc4627238a24505871ccb6495e9dc1f71abe55e8516a65187203/waferslim-1.0.2-py3.1.zip#md5=0a64e550f67b3e02d99373d83498547d

RUN cd /binaries && \
    curl -o waferslim.zip -L \
    $W_URL && \
    unzip waferslim && \
    cd /binaries/waferslim-1.0.2 && python setup.py install

CMD ["java","-jar","/binaries/fitnesse-standalone.jar", "-v", "-p", "8081"]
