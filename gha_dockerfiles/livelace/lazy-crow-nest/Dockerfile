FROM            docker.io/python:3.9-buster

ENV             LCN_TEMP="/tmp/lcn"
ENV             PIP_CONFIG_FILE="pip.conf"

# copy dataset.
RUN             mkdir -p "/data"

COPY            "data/spark/lazy-crow-nest/job-hh-common-rss-elastic.pickle" "/data/common.pickle"
COPY            "data/spark/lazy-crow-nest/job-hh-it-rss-elastic.pickle" "/data/it.pickle"

# create user.
RUN             useradd -m -u 1000 -s "/bin/bash" "lcn"

USER            "lcn"

# install app.
COPY            "work" "$LCN_TEMP"

RUN             cd "$LCN_TEMP" && \
                pip install --no-cache-dir --user -r "requirements.txt" && \
                pip install --no-cache-dir --user . && \
                rm -rf "$LCN_TEMP"

WORKDIR         "/home/lcn"

CMD             ["/home/lcn/.local/bin/lazy-crow-nest"]