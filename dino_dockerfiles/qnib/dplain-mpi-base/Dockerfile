FROM qnib/dplain-init

ENV SKIP_ENTRYPOINTS=true

COPY etc/apt/preferences.d/gcc \
     etc/apt/preferences.d/g++ \
     /etc/apt/preferences.d/
RUN apt-get update \
 && apt-get install -y wget gcc make g++ \
 && apt-get autoclean
