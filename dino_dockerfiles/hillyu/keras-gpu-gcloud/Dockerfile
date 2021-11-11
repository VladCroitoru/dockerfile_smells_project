FROM hillyu/keras-gpu:latest
RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"; echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list; curl https://packages.cloud.google.com/apt/doc/apt-key.gpg |apt-key add -; apt-get update && apt-get install -y --no-install-recommends google-cloud-sdk
RUN gcloud config set core/disable_usage_reporting true && \
			   gcloud config set component_manager/disable_update_check true && \
			   gcloud config set metrics/environment github_docker_image
RUN apt-get install -y --no-install-recommends vim-nox git python3-sqlalchemy
VOLUME ["/root/.config","/root/.jupyter"]
