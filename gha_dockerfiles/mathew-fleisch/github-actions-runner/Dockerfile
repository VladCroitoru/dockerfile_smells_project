FROM mathewfleisch/tools:v0.1.41
LABEL maintainer="Mathew Fleisch <mathew.fleisch@gmail.com>"

ENV KUBECONFIG_CONTENTS ""
ENV GIT_PAT ""
ENV GIT_OWNER ""
ENV GIT_REPO ""
ENV PING ""
ENV LABELS "container-runner"
ENV RUNNER_WORKDIR "_work"
ENV ASDF_DATA_DIR=/opt/asdf

# Install asdf dependencies. See https://github.com/mathew-fleisch/tools for base container tools
USER github
WORKDIR /home/github
COPY --chown=github:github .tool-versions ./.tool-versions
COPY --chown=github:github pin ./pin
RUN sudo chown github:github -R ${ASDF_DATA_DIR} \
    && . ${ASDF_DATA_DIR}/asdf.sh \
    && asdf update \
    && echo "$(while IFS= read -r line; do asdf plugin add $(echo "$line" | awk '{print $1}'); done < .tool-versions )" \
    && asdf install
# Install docker buildx dependencies
RUN mkdir -p .docker \
    && sudo chown -R github:github .docker \
    && docker buildx create --name mbuilder || true \
    && docker buildx use mbuilder \
    && docker buildx inspect --bootstrap

# Source asdf and execute entrypoint
COPY --chown=github:github entrypoint.sh ./entrypoint.sh
RUN sudo chmod u+x ./entrypoint.sh
CMD /bin/sh -c ". ${ASDF_DATA_DIR}/asdf.sh && sudo chmod 666 /var/run/docker.sock && /home/github/entrypoint.sh"


