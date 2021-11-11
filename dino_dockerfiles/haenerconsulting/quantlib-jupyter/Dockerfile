ARG tag=latest
FROM lballabio/quantlib-python3:${tag}
MAINTAINER Patrick Haener <contact@haenerconsulting.com>
ARG VERSION
ARG BUILD_DATE
ARG VCS_REF
ARG GIT_COMMIT=unspecified
LABEL Description="A Jupyter notebook server with the QuantLib Python module available"
LABEL org.label-schema.version=$VERSION
LABEL org.label-schema.vcs-ref=$VCS_REF
LABEL org.label-schema.vcs-url=https://github.com/haenerconsulting/quantlib-jupyter
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL git_commit=$GIT_COMMIT

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y wget python3-distutils \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN wget https://bootstrap.pypa.io/get-pip.py \
 && python3 get-pip.py \
 && rm get-pip.py

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt && rm /requirements.txt
RUN jupyter-nbextension install rise --py --sys-prefix

ADD templates /notebooks/templates
RUN mkdir /notebooks/user
VOLUME /notebooks/user

EXPOSE 8888

CMD jupyter-notebook --no-browser --allow-root --ip=0.0.0.0 --port=8888 --notebook-dir=/notebooks --NotebookApp.token=""
