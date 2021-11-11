FROM python:3.8-slim

# Checkout and install dagster libraries needed to run the gRPC server
# exposing your repository to dagit and dagster-daemon, and to load the DagsterInstance

WORKDIR /tmp
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set $DAGSTER_HOME and copy dagster instance there
ENV DAGSTER_HOME=/opt/dagster/dagster_home

# Create basedosdados directories and mount directories for actual credentials
RUN mkdir -p $DAGSTER_HOME \
  && mkdir -p /root/.basedosdados/templates \
  && mkdir -p /root/.basedosdados_mount/credentials \
  && touch /root/.basedosdados_mount/config.toml \
  && ln -s /root/.basedosdados_mount/config.toml /root/.basedosdados/config.toml \
  && ln -s /root/.basedosdados_mount/credentials /root/.basedosdados/credentials

COPY .dagster_workspace/dagster.yaml $DAGSTER_HOME

# Add repository code
WORKDIR /opt/dagster/app
COPY bases/ /opt/dagster/app/bases/
COPY repositories/ /opt/dagster/app/repositories/

# Run dagster gRPC server on port 4000
EXPOSE 3030

# CMD allows this to be overridden from run launchers or executors that want
# to run other commands against your repository
CMD ["dagster", "api", "grpc", "-h", "0.0.0.0", "-p", "3030", "-f", "repositories/repository.py"]
