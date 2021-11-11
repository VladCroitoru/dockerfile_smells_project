FROM alpine:3.4
MAINTAINER Shingo Omura <everpeace@gmail.com>

# dependent packages
ENV dep_pkgs 'curl git bash file sudo openssh openssl ruby ruby-dev libxml2-dev libxslt-dev'

# tool versions
ENV MECAB_VERSION         0.996
ENV IPADIC_VERSION        2.7.0-20070801
ENV WORD2VEC_GIT_BRANCH   master
ENV CONVERTVEC_GIT_BRANCH master
ENV WP2TEXT_VERSION       0.8.0

# tool download urls
ENV mecab_url          https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE
ENV ipadic_url         https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM
ENV word2vec_git_url   https://github.com/svn2github/word2vec.git
ENV convertvec_git_url https://github.com/marekrei/convertvec

# default environment varialbes for build-embedding-jawiki.sh
ENV WP2TXT_OPTIONS   -f 99
ENV MECAB_REPROCESS  0
ENV MECAB_OPTIONS    -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/ -b 81920
ENV WORD2VEC_OPTIONS -cbow 0 -size 200 -threads 2
ENV JAWIKI_URL       https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2
ENV JAWIKI_FILENAME  jawiki-pages-articles.xml.bz2
ENV OUTPUT_DIR       /var/jawiki

# Install dependent tools
RUN apk add --update --no-cache build-base
RUN apk add --update --no-cache ${dep_pkgs}

# Install MeCab
RUN curl -SL -o mecab-${MECAB_VERSION}.tar.gz ${mecab_url} \
  && tar zxf mecab-${MECAB_VERSION}.tar.gz \
  && cd mecab-${MECAB_VERSION} \
  && ./configure --enable-utf8-only --with-charset=utf8 \
  && make \
  && make install \
  && cd

# Install IPA dic
RUN curl -SL -o mecab-ipadic-${IPADIC_VERSION}.tar.gz ${ipadic_url} \
  && tar zxf mecab-ipadic-${IPADIC_VERSION}.tar.gz \
  && cd mecab-ipadic-${IPADIC_VERSION} \
  && ./configure --with-charset=utf8 \
  && make \
  && make install \
  && cd

# Install NEologd
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
  && mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -y

# Install word2vec
RUN git clone ${word2vec_git_url} \
  && cd word2vec \
  && git checkout ${WORD2VEC_GIT_BRANCH} \
  && make \
  && cp word2vec /usr/local/bin/ \
  && cp word2phrase /usr/local/bin/ \
  && cp distance /usr/local/bin/ \
  && cp word-analogy /usr/local/bin/ \
  && cp compute-accuracy /usr/local/bin/ \
  && cd

# Install convertvec
RUN git clone ${convertvec_git_url} \
  && cd convertvec \
  && make \
  && cp convertvec /usr/local/bin/ \
  && cd

# Install wp2txt
RUN gem install wp2txt -v ${WP2TEXT_VERSION} --no-document

# Install build-embedding-jawiki.sh
ADD build-embedding-jawiki.sh ./
RUN chmod +x build-embedding-jawiki.sh

# Remove build files
RUN rm -rf \
    mecab-${MECAB_VERSION}* \
    mecab-ipadic-${IPADIC_VERSION}* \
    mecab-ipadic-neologd \
    word2vec \
    convertvec

# test if tools are properly installed or downloaded.
RUN which mecab && mecab --version
RUN which word2vec && word2vec
RUN which wp2txt && wp2txt --version
RUN which convertvec && convertvec --help

VOLUME ${OUTPUT_DIR}
CMD /build-embedding-jawiki.sh
