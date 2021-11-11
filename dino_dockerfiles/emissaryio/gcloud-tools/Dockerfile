FROM emissaryio/node-python:1.0.1

WORKDIR /google
ENV GOOGLE_DIR /google

# gcloud
RUN wget -q https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-163.0.0-linux-x86_64.tar.gz -O gcloud-sdk.tar.gz \
    && tar xfz gcloud-sdk.tar.gz \
    && rm gcloud-sdk.tar.gz

# gcloud app-engine
RUN google-cloud-sdk/bin/gcloud components install -q \
    app-engine-python \
    app-engine-python-extras \
    && rm -rf google-cloud-sdk/.install/.backup

ENV PYTHONPATH $PYTHONPATH:$GOOGLE_DIR/google-cloud-sdk/platform/google_appengine/

# install deployment script dependencies
RUN pip install --no-cache-dir \
    pyyaml \
    requests

# cloud_sql_proxy
RUN wget -q https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy \
    && chmod +x cloud_sql_proxy \
    && mkdir /cloudsql

WORKDIR /

