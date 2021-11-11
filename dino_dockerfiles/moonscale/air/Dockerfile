FROM maven:3.2-jdk-8

ENV AIR_SDK_VERSION=25.0.0.134
ENV AIR_SDK_DOWNLOAD_URL=http://fpdownload.macromedia.com/air/win/download/25.0/AdobeAIRSDK.zip

# Install Wine, Xvfb & AIR SDK
RUN dpkg --add-architecture i386 \
  && apt-get update \
  && apt-get install -y \
    wine \
    wine32 \
    xvfb \
  && rm -rf /var/lib/apt/lists/* \
  && curl ${AIR_SDK_DOWNLOAD_URL} > /tmp/AdobeAIRSDK.zip \
  && mkdir -p /usr/local/air/sdk \
  && cd /usr/local/air/sdk \
  && unzip /tmp/AdobeAIRSDK.zip \
  && rm /tmp/AdobeAIRSDK.zip

# Add adl wrapper
COPY ./adl /usr/local/air/sdk/bin/adl
RUN ln -s /usr/local/air/sdk/bin/adl /usr/local/bin/adl
