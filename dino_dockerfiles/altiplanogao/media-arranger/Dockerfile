ARG PYTHON3_IMG=python:3.4-slim
#ARG PYTHON3_IMG=armhf/python:3.6-slim
FROM ${PYTHON3_IMG}

RUN apt-get clean && rm -rf /var/lib/apt/lists/* && \
    apt-get update && apt-get install -y curl && mkdir -p /appspace/config
ADD ./config/settings.yml /appspace/config
VOLUME ["/appspace/src", "/appspace/dst", "/appspace/logs", "/appspace/config"]

ARG URL_TMPL=https://www.sno.phy.queensu.ca/~phil/exiftool/
RUN /bin/bash -c "export EXIF_TOOL_FN=`curl -s ${URL_TMPL} | grep ".tar.gz" | sed 's|.*href="\(.*\)\.tar\.gz".*|\1|g'` && \
    echo Tool name: \${EXIF_TOOL_FN}  && \
    export EXIF_TOOL_URL=${URL_TMPL}\${EXIF_TOOL_FN}.tar.gz && \
    echo Url: \${EXIF_TOOL_URL} && \
    curl -O \${EXIF_TOOL_URL} && \
    tar xzf \${EXIF_TOOL_FN}.tar.gz && mv \${EXIF_TOOL_FN} Image-ExifTool && rm -rf \${EXIF_TOOL_FN}.tar.gz && \
     ls -la"

ENV PATH "/Image-ExifTool:${PATH}"
RUN exiftool -ver

ADD ./src /media-arranger
RUN pip install --trusted-host pypi.python.org -r /media-arranger/requirements.txt

COPY ./docker-entry.sh /media-arranger/
RUN chmod +x /media-arranger/*.sh
WORKDIR /media-arranger

ENTRYPOINT ["/media-arranger/docker-entry.sh"]
# CMD ["python", "entry.py", "-c", "/appspace/config"]
