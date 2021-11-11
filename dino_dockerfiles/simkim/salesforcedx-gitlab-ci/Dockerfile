FROM simkim/salesforcedx
VOLUME /app
WORKDIR /app
RUN apt-get update && apt-get install -y \
  python \
  jq \
  && rm -rf /var/lib/apt/lists/*

# sfdx environment
ENV SFDX_AUTOUPDATE_DISABLE true
ENV SFDX_USE_GENERIC_UNIX_KEYCHAIN true
ENV SFDX_DOMAIN_RETRY 300
# build environment
ENV CI_PROJECT_DIR /app
ENV CI_SFDX_ORG ciorg
ENV CI_SFDX_KEY assets/server.key
ENV CI_SFDX_SCRATCH_DEF config/project-scratch-def.json
COPY sfdx-test.sh /usr/local/bin/
CMD bash
