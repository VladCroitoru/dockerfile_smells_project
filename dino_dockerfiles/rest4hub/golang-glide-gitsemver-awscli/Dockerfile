FROM rest4hub/golang-glide:gitsemver

RUN wget https://oss.oracle.com/el4/unzip/unzip.tar && \
    tar xvf unzip.tar
RUN wget https://s3.amazonaws.com/aws-cli/awscli-bundle.zip && \
    ./unzip awscli-bundle.zip  && \
    ./awscli-bundle/install -b /bin/aws