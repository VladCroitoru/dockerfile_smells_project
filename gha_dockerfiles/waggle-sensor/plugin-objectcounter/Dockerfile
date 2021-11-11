FROM waggle/plugin-base:1.1.1-ml

COPY requirements.txt /app/
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# apex supports multi precision training/inference for Tensor cores
# if we want to use fp16 models we need this as long as we use Nvidia's torch hub
# NOTE: pip3 install apex does not work as of Oct 2020 so install from git
# NOTE: installing apex requires nvcc which isn't in runtime Nvidia Docker
#       it needs devel version of Docker
# NOTE: Pytorch 1.6.0 does not support fp16 on CPU
#       https://github.com/open-mmlab/mmdetection/issues/2951#issuecomment-641024130
#RUN cd /tmp \
#  && git clone https://www.github.com/nvidia/apex \
#  && cd apex \
#  && python3 setup.py install \
#  && rm -rf /tmp/apex
#
#COPY apex-0.1-py3-none-any.whl /tmp/
#RUN cd /tmp \
# && pip3 install apex-0.1-py3-none-any.whl

COPY PyTorch /app/PyTorch
COPY hubconf.py app.py category_names.txt /app/

ARG SAGE_STORE_URL="https://osn.sagecontinuum.org"
ARG BUCKET_ID_MODEL="cafb2b6a-8e1d-47c0-841f-3cad27737698"

ENV SAGE_STORE_URL=${SAGE_STORE_URL} \
    BUCKET_ID_MODEL=${BUCKET_ID_MODEL}

RUN sage-cli.py storage files download ${BUCKET_ID_MODEL} coco_ssd_resnet50_300_fp32.pth --target /app/coco_ssd_resnet50_300_fp32.pth

WORKDIR /app
ENTRYPOINT ["python3", "/app/app.py"]
