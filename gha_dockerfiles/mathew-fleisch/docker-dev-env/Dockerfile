FROM mathewfleisch/tools:v0.1.41
LABEL maintainer="Mathew Fleisch <mathew.fleisch@gmail.com>"

ENV ASDF_DATA_DIR /opt/asdf

USER root
# Install asdf dependencies
WORKDIR /root
COPY .tool-versions ./.tool-versions
COPY pin ./pin
RUN . ${ASDF_DATA_DIR}/asdf.sh  \
    && asdf update \
    && echo "$(while IFS= read -r line; do asdf plugin add $(echo $line | awk '{print $1}'); done < .tool-versions)" \
    && asdf install

CMD /bin/bash -c '. ${ASDF_DATA_DIR}/asdf.sh && for plugin in $(asdf plugin list); do asdf global $plugin $(asdf list $plugin | sort -V | tail -1); done && /bin/bash'
