FROM waggle/plugin-base:1.1.1-ml

RUN apt-get update \
  && apt-get install -y \
  ffmpeg \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip3 install --no-cache-dir --upgrade -r /app/requirements.txt

COPY deep_sort/ /app/deep_sort
COPY detection/ /app/detection
COPY tool/ /app/tool
COPY app.py app_utils.py siamese_net.py /app/

ARG SAGE_STORE_URL="https://osn.sagecontinuum.org"
ARG BUCKET_ID_MODEL="cafb2b6a-8e1d-47c0-841f-3cad27737698"

ENV SAGE_STORE_URL=${SAGE_STORE_URL} \
    BUCKET_ID_MODEL=${BUCKET_ID_MODEL}

RUN sage-cli.py storage files download ${BUCKET_ID_MODEL} model640.pt --target /app/model640.pt \
  && sage-cli.py storage files download ${BUCKET_ID_MODEL} yolov4.cfg --target /app/yolov4.cfg \
  && sage-cli.py storage files download ${BUCKET_ID_MODEL} yolov4.weights --target /app/yolov4.weights

WORKDIR /app
ENTRYPOINT ["python3", "-u", "/app/app.py"]
