## NOTE: these defaults are not used by travis!
## you *must* update the .travis.yml file to change the dripline-python version
ARG img_user=driplineorg
ARG img_repo=dripline-python
ARG img_tag=v3.10.1

#FROM project8/dripline-python
FROM ${img_user}/${img_repo}:${img_tag}

COPY . /dragonfly
RUN apt-get install -y python3-psycopg2 libpq-dev
RUN pip3 install /dragonfly[colorlog,database,slack]
