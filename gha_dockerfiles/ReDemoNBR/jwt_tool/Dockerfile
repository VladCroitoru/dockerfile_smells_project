FROM python:3-bullseye

WORKDIR /opt/jwt_tool

COPY jwt_tool.py LICENSE requirements.txt ./

RUN apt-get update && \
    apt-get upgrade --yes && \
    pip install --no-cache-dir -r requirements.txt && \
    rm --recursive --force /var/lib/apt/lists/* && \
    chmod +x jwt_tool.py && \
    ln --symbolic /opt/jwt_tool/jwt_tool.py /usr/local/bin/jwt-tool && \
    ln --symbolic jwt-tool /usr/local/bin/jwt_tool && \
    # generate initial config
    jwt-tool --bare || echo "generated initial config"

ENTRYPOINT ["jwt-tool"]

CMD ["-h"]
