FROM homeassistant/home-assistant:0.52.1

RUN set -e && \
    pip uninstall -y python_openzwave && \

    pip3 install --upgrade cython==0.24.1 && \
    pip3 install --no-cache-dir python_openzwave==0.4.0.31 --install-option="--flavor=ozwdev" && \
    mkdir -p /usr/local/share/python-openzwave && \
    ln -s /usr/local/lib/python3.6/site-packages/python_openzwave/ozw_config /usr/local/share/python-openzwave/config
