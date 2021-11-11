FROM amazonlinux:2
COPY .amazon-linux-bi-build /
COPY amzn2-ec2-packages.txt dacut-extras.txt dacut-python-extras.txt /tmp/
RUN yum update -y && \
    yum install -y $(cat /tmp/amzn2-ec2-packages.txt) && \
    yum groupinstall -y 'AWS Tools' && \
    yum groupinstall -y 'Development Tools' && \
    yum install -y $(cat /tmp/dacut-extras.txt) && \
    pip-3 install $(cat /tmp/dacut-python-extras.txt) && \
    rm /tmp/*.txt
CMD /bin/zsh
