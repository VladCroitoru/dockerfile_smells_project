# FROM python:2-alpine
FROM python:2

# You can configure the way jrnl behaves in a configuration file. By default, this is ~/.jrnl_config. If you have the XDG_CONFIG_HOME variable set, the configuration file will be saved under $XDG_CONFIG_HOME/jrnl.
ENV XDG_CONFIG_HOME=/jrnlfiles

RUN apt update && apt install nano

RUN mkdir /jrnlfiles
VOLUME /jrnlfiles

RUN pip install jrnl

CMD [ "jrnl" ]