FROM hashicorp/terraform:light

ENV ORACLE_BARE_METAL_CLOUD=1.0.16

RUN apk add bash openssl && \
      wget https://github.com/oracle/terraform-provider-baremetal/releases/download/v${ORACLE_BARE_METAL_CLOUD}/linux.tar.gz && \
      mkdir /usr/local/oracle && \
      tar -C /usr/local/oracle -xzf linux.tar.gz && \
      rm -rf /usr/local/linux.tar.gz && \
      echo "providers { baremetal = \"/usr/local/oracle/linux_386/terraform-provider-baremetal\" }" | tee ~/.terraformrc
