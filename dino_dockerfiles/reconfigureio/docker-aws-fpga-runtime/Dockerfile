FROM ubuntu:18.04
ENV AWS_FPGA_VERSION=1.4.5
RUN apt-get update && apt-get install -y --no-install-recommends \
		ca-certificates \
		make \
        gcc \
        sudo \
        libc6-dev \
        wget \
	&& rm -rf /var/lib/apt/lists/* && ln -s /usr/lib/ /usr/lib64 \
    && cd /tmp \
    && wget -q -O - https://github.com/aws/aws-fpga/archive/v$AWS_FPGA_VERSION.tar.gz | tar -xz \
    && SDK_DIR=/tmp/aws-fpga-$AWS_FPGA_VERSION/sdk bash -c "source /tmp/aws-fpga-$AWS_FPGA_VERSION/sdk_setup.sh" \
    && rm -rf /tmp/aws-fpga-$AWS_FPGA_VERSION
