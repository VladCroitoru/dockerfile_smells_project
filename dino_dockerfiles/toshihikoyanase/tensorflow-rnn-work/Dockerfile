FROM b.gcr.io/tensorflow/tensorflow-full:latest

MAINTAINER Toshihiko Yanase <toshihiko.yanase@gmail.com>

#
WORKDIR /tensorflow
RUN bazel build -c opt tensorflow/models/rnn/ptb:ptb_word_lm
