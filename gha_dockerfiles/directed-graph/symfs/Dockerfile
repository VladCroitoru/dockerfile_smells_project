FROM implementing/bazel:latest

WORKDIR /github/directed-graph/symfs

# Actual items are based on what's defined in .dockerignore.
COPY . .

RUN bazel build :symfs.par && \
    bazel test --test_output=all :all && \
    mkdir -p /usr/local/bin/everchanging && \
    cp bazel-bin/symfs.par /usr/local/bin/symfs.par && \
    bazel clean

ENTRYPOINT ["/usr/local/bin/symfs.par"]
