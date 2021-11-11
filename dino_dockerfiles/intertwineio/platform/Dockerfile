FROM intertwineio/base
# # ======================================================================
# #  Setup platform
# # ======================================================================
COPY . /opt/repos/platform
WORKDIR /opt/repos/platform
ENV WORKON_HOME /root/.envs

# Install package
RUN set -ex \
    && cd /opt/repos/platform \
    && pip install -U pip vex \
    && vex -m --python python venv pip install --process-dependency-links -e .[all] \
    && vex -m --python python3 venv3 pip install --process-dependency-links -e .[all] \
    && apt-get clean autoclean \
    && apt-get autoremove -y \
    && rm -Rf .eggs \
    && rm -rf /var/lib/{apt,dpkg,cache,log}/
    # && vex -m --python pypy venvpy pip install --process-dependency-links -e .[all] \

CMD ["vex", "venv", "circusd", "circus.ini"]

ARG VERSION=Undefined
LABEL org.label-schema.vendor="Intertwine.io" \
      org.label-schema.url="https://intertwine.io" \
      org.label-schema.name="Intertwine platform" \
      org.label-schema.description="Untangling the World's Problems" \
      org.label-schema.version=$VERSION
