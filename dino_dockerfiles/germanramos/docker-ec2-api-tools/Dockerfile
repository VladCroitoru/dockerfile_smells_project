FROM rawmind/alpine-jvm8:1.8.92-5

RUN wget http://s3.amazonaws.com/ec2-downloads/ec2-api-tools.zip && \
    mkdir /usr/local/ec2 && \
    unzip ec2-api-tools.zip -d /usr/local/ec2

ENV JAVA_HOME=/opt/jre
ENV EC2_HOME=/usr/local/ec2/ec2-api-tools-1.7.5.1
ENV PATH=$PATH:$EC2_HOME/bin

ENTRYPOINT ["bash"]
