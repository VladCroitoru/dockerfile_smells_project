FROM amazon/aws-cli:2.2.46

RUN yum install wget-1.14 git-2.23.4 -y && \
    yum clean all
RUN wget https://github.com/mozilla/sops/releases/download/v3.7.1/sops-3.7.1-1.x86_64.rpm --no-verbose
RUN rpm -i sops-3.7.1-1.x86_64.rpm

WORKDIR /opt/management

COPY [ "./management", "." ]

ENTRYPOINT ["/bin/bash", "-c"]
