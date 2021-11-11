FROM dcagatay/ubuntu-dind:18.04

ENV DEBIAN_FRONTEND=noninteractive
RUN echo "APT::Get::Assume-Yes \"true\";" > /etc/apt/apt.conf.d/90assumeyes

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    jq \
    git \
    iputils-ping \
    libcurl4 \
    libicu60 \
    libunwind8 \
    netcat \
    libssl1.0 \
    openssh-client \
    wget \
    iptables \
    gss-ntlmssp \
    apt-utils \
  && rm -rf /var/lib/apt/lists/*

# Install Azure Cli
RUN curl -LsS 'https://aka.ms/InstallAzureCLIDeb' | bash \
  && rm -rf /var/lib/apt/lists/*

# Install .NET CORE runtime
RUN curl -fSL --retry 3 'https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb' -o /tmp/packages-microsoft-prod.deb && \
    dpkg -i /tmp/packages-microsoft-prod.deb && \
    rm -rf /tmp/packages-microsoft-prod.deb && \
    apt-get update && apt-get install -y --no-install-recommends \
      dotnet-runtime-3.1

ARG TARGETARCH=amd64
ARG AGENT_VERSION=2.188.3

WORKDIR /azp
RUN if [ "$TARGETARCH" = "amd64" ]; then \
      AZP_AGENTPACKAGE_URL=https://vstsagentpackage.azureedge.net/agent/${AGENT_VERSION}/vsts-agent-linux-x64-${AGENT_VERSION}.tar.gz; \
    else \
      AZP_AGENTPACKAGE_URL=https://vstsagentpackage.azureedge.net/agent/${AGENT_VERSION}/vsts-agent-linux-${TARGETARCH}-${AGENT_VERSION}.tar.gz; \
    fi; \
    curl -LsS "$AZP_AGENTPACKAGE_URL" | tar -xz

RUN apt-get autoremove -y \
  && apt-get autoclean -y \
  && rm -rf /var/lib/apt/lists/*

COPY ./start.sh .
RUN chmod +x start.sh

COPY services.d /etc/services.d
