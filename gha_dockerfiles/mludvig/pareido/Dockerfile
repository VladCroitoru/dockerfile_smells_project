### Builder container
FROM openvino/ubuntu20_runtime:2021.4 AS builder

WORKDIR /home/openvino
ADD --chown=openvino requirements-frozen.txt ./
RUN \
  python3 -m venv venv && \
  source venv/bin/activate && \
  pip3 install wheel && \
  pip3 install -r requirements-frozen.txt && \
  rm -rf $HOME/.cache

ARG MODELS_TXT=models-small.txt
ADD ${MODELS_TXT} ./
RUN \
  source venv/bin/activate && \
  pip3 install -r ${MODELS_TXT} \
    -f https://modelplace.s3.amazonaws.com/index.html \
    -f https://download.pytorch.org/whl/torch_stable.html

### Target container
FROM openvino/ubuntu20_runtime:2021.4

MAINTAINER Michael Ludvig (https://github.com/mludvig)

WORKDIR /home/openvino
RUN echo "source venv/bin/activate" >> .bashrc

EXPOSE 8000

COPY --from=builder --chown=openvino /home/openvino/venv ./venv

ADD --chown=openvino scripts ./scripts

# Add the source code
ADD --chown=openvino pareido pareido

CMD "scripts/docker-server.sh"
