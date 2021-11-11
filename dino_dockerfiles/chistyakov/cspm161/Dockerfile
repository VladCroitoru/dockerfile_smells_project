FROM debian:latest

WORKDIR /usr/local/cspm161/
VOLUME /usr/local/cspm161/downloaded_files

RUN apt-get update && apt-get install -y curl

ADD proxy_cache_hypothesis_checker.sh /usr/local/cspm161/proxy_cache_hypothesis_checker.sh

ENTRYPOINT ["bash", "/usr/local/cspm161/proxy_cache_hypothesis_checker.sh"]
