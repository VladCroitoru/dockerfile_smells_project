FROM jruby:1.7.21-jdk
MAINTAINER Sébastien Prunier <sebastien.prunier@gmail.com>

RUN apt-get update && apt-get install -y gcc g++ make libarchive-dev python2.7 python-pip --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN \
  gem install opener-language-identifier && \
  gem install opener-tokenizer && \
  gem install opener-pos-tagger && \
  gem install opener-tree-tagger && \
  gem install opener-polarity-tagger && \
  gem install opener-property-tagger && \
  gem install opener-constituent-parser && \
  gem install opener-ner && \
  gem install opener-coreference && \
  gem install opener-ned && \
  gem install opener-opinion-detector && \
  gem install opener-opinion-detector-basic && \
  gem install opener-kaf2json && \
  gem install opener-outlet && \
  gem install opener-scorer

CMD ["/bin/bash"]
