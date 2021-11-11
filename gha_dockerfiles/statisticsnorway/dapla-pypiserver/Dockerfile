FROM jupyter/all-spark-notebook:95ccda3619d0 as package-downloader

USER jovyan
RUN python3 -m pip install --upgrade pip
USER root
RUN apt update && \
    apt-get -y clean all && \
    apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y dist-upgrade && \
    apt-get install --no-install-recommends -y openssh-client r-cran-rglpk glpk-utils libglpk-dev libpoppler-cpp-dev \
    zlib1g-dev libgit2-dev libtesseract-dev libleptonica-dev && \
    rm -rf /var/lib/apt/lists/*
COPY Packages.txt /packages.txt
ENV SERVED_PACKAGES_DIRECTORY=/home/jovyan/packages
RUN mkdir $SERVED_PACKAGES_DIRECTORY
RUN echo "" > $SERVED_PACKAGES_DIRECTORY/__init__.py
RUN chown -R jovyan /home/jovyan
USER jovyan
RUN export PYTHONPATH="${PYTHONPATH}:$SERVED_PACKAGES_DIRECTORY"
RUN while read -r in; do python3 -m pip download -d "$SERVED_PACKAGES_DIRECTORY" "$in"; done < "/packages.txt"

FROM python:3.9-alpine

USER root
RUN apk update && apk upgrade && \
    apk --update --upgrade add gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev libxml2 libxslt geos geos-dev gdal gdal-dev \
    make automake gcc g++ subversion python3-dev && \
    apk add --no-cache --upgrade bash && \
    apk add bash-doc bash-completion util-linux pciutils usbutils coreutils binutils findutils grep

RUN python3 -m pip install --upgrade pip wheel setuptools pypiserver passlib
COPY Packages.txt /packages.txt

RUN addgroup -S servergroup && adduser -S serveruser -G servergroup
ENV SERVED_PACKAGES_DIRECTORY=/home/serveruser/packages
RUN mkdir $SERVED_PACKAGES_DIRECTORY && \
    echo "" > $SERVED_PACKAGES_DIRECTORY/__init__.py && \
    export PYTHONPATH="${PYTHONPATH}:$SERVED_PACKAGES_DIRECTORY"

COPY --from=package-downloader /home/jovyan/packages $SERVED_PACKAGES_DIRECTORY
RUN chown -R serveruser $SERVED_PACKAGES_DIRECTORY && \
    chmod -R 554 $SERVED_PACKAGES_DIRECTORY && \
    mkdir /credentials
COPY htpasswd.txt credentials/htpasswd.txt
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
USER serveruser

EXPOSE 8080

CMD ["/bin/bash", "/entrypoint.sh"]
