From debian

RUN apt-get update -y && apt-get install libapparmor-dev -y

add . /plugin
workdir /plugin

entrypoint ["sh", "start.sh"]
