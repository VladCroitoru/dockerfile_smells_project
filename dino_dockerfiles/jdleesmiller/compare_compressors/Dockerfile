#
# Note: The ruby 2.4.0 image uses Debian jessie, which does not have many of
# the newer compression algorithms packaged, so we'd have to backport them.
# Instead, I'm just installing ubuntu 16.04 (xenial), which does have the
# required compressor packages, and using the system ruby.
#
FROM ubuntu:xenial-20190610

RUN set -ex &&\
  apt-get update &&\
  apt-get install --no-install-recommends -y ruby ruby-dev bundler time \
    brotli bzip2 p7zip xz-utils zstd &&\
  rm -rf /var/lib/apt/lists/* &&\
  useradd --user-group --create-home --shell /bin/false app

ENV HOME=/home/app

COPY . $HOME/compare_compressors
RUN chown -R app:app $HOME/*

WORKDIR $HOME/compare_compressors
USER app
RUN bundle --no-cache --deployment --path $HOME/bundle

ENTRYPOINT ["bundle", "exec", "bin/compare_compressors"]
