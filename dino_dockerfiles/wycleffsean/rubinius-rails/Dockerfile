FROM rubinius/docker
RUN apt-get update && \
    apt-get install -y \
      build-essential patch ruby-dev zlib1g-dev liblzma-dev libpq-dev
RUN gem install rails:4.2.5 --no-document
RUN gem install pg --no-document
CMD ["bash"]
