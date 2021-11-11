FROM mozmeao/bedrock:prod-latest
USER root
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY settings_local.py bedrock/settings/local.py
COPY update_etags.py sitemap_utils.py bin/run-generator.sh ./
ARG USER_ID=1000:1000
ENV USER_ID=${USER_ID}
RUN chown -R "${USER_ID}" /app
USER ${USER_ID}
