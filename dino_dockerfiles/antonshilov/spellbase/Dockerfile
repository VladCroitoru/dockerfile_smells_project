FROM python:3.6.5-stretch
LABEL maintainer="Anton Shilov <vaccum121@gmail.com>" \
      description="Base image with dependencies for spellcheck"
RUN apt-get update &&\
    apt-get -y install aspell-ru enchant python3-pip &&\
    pip3 install nltk &&\
    python3 -c "import nltk; nltk.download('punkt', download_dir='/usr/share/nltk_data')"