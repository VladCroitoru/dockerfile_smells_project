# Docker file for the nirs_sim_app plugin app

FROM nvidia/cuda:9.1-devel as builder

WORKDIR /usr/src/mcx
COPY ["mcx", "/usr/src/mcx"]
RUN make lib/libmcx && mv lib/libmcx.so pymcx/


FROM python:3-slim
MAINTAINER fnndsc "dev@babymri.org"

LABEL com.nvidia.volumes.needed="nvidia_driver"
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

ENV APPROOT="/usr/src/nirs_sim_app"  VERSION="0.1"
COPY ["nirs_sim_app", "${APPROOT}"]
COPY ["requirements.txt", "${APPROOT}"]
COPY --from=builder ["/usr/src/mcx/pymcx", "${APPROOT}/pymcx"]

WORKDIR $APPROOT

RUN apt-get update && \
    apt-get install -y --no-install-recommends libgomp1 && \
    pip3 install --no-cache-dir -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["python3"]
CMD ["nirs_sim_app.py", "--json"]
