# syntax=docker/dockerfile:1.3.0-labs
ARG username=worker
ARG work_dir=/home/$username/work
ARG gid=1000
ARG uid=1001

FROM adoptopenjdk:15.0.2_7-jdk-hotspot as worker
ARG username
ARG work_dir
ARG gid
ARG uid

# Install xvfb so that a GUI (and GUI tests) can run
RUN apt-get -qq update && \
    DEBIAN_FRONTEND=noninteractive apt-get -qq -o=Dpkg::Use-Pty=0 install \
      libxrender1 libxtst6 libxi6 \
      fontconfig \
      xvfb \
      && rm -rf /var/lib/apt/lists/*
RUN mkdir /tmp/.X11-unix && chmod 1777 /tmp/.X11-unix
COPY --chown=root scripts/simple-xvfb-run.sh /usr/bin/simple-xvfb-run

RUN addgroup --system $username --gid $gid && \
    adduser --system $username --ingroup $username --uid $uid

USER $username
RUN mkdir -p $work_dir
WORKDIR $work_dir


FROM worker as gradle
ARG username
# The single use daemon will be unavoidable in future so don't waste time trying to prevent it
ENV GRADLE_OPTS='-Dorg.gradle.daemon=false'

# Download gradle in a separate step to benefit from layer caching
COPY --chown=$username gradle/wrapper gradle/wrapper
COPY --chown=$username gradlew gradlew
RUN ./gradlew --version

FROM gradle as builder
ARG username
ARG gid
ARG uid

COPY --chown=$username . .

ARG gradle_cache_dir=/home/$username/.gradle/caches

# Do all the downloading in one step...
RUN --mount=type=cache,target=$gradle_cache_dir,gid=$gid,uid=$uid \
    ./gradlew --no-watch-fs --stacktrace downloadDependencies

# So the actual build can run without network access. Proves no tests rely on external services.
RUN --mount=type=cache,target=$gradle_cache_dir,gid=$gid,uid=$uid \
    --network=none \
    set +e; \
    simple-xvfb-run ./gradlew --no-watch-fs --stacktrace --offline build; \
    echo $? > build_result;


FROM scratch as build-reports
ARG work_dir

COPY --from=builder $work_dir/build/reports ./build-reports

# The builder step is guaranteed not to fail, so that the worker output can be tagged and its
# contents (build reports) extracted.
# You run this as:
# `docker build . --target build-reports --output build-reports && docker build .`
# to retrieve the build reports whether or not the previous line exited successfully.
# Workaround for https://github.com/moby/buildkit/issues/1421
FROM builder as checker
RUN build_result=$(cat build_result); \
    if [ "$build_result" -eq 137 ]; then >&2 echo "The build failed with exit status $build_result, you probably need to give Docker more memory"; \
    elif [ "$build_result" -gt 0 ]; then >&2 echo "The build failed with exit status $build_result, check output of builder stage"; fi; \
    exit "$build_result"


FROM worker as end-to-end-tests
ARG username
ARG work_dir

COPY --from=checker --chown=$username $work_dir/end-to-end-tests/build/install/end-to-end-tests/lib/external ./external
COPY --from=checker --chown=$username $work_dir/end-to-end-tests/build/install/end-to-end-tests/lib/internal ./internal
COPY --from=checker --chown=$username $work_dir/end-to-end-tests/build/install/end-to-end-tests/lib/end-to-end-tests.jar .

ENTRYPOINT ["java", "-jar", "--illegal-access=deny", "-ea", "end-to-end-tests.jar"]


FROM worker as auction-xmpp-integration-tests
ARG username
ARG work_dir

COPY --from=checker --chown=$username $work_dir/app-src/auction/xmpp-integration-tests/build/install/auction-xmpp-integration-tests/lib/external ./external
COPY --from=checker --chown=$username $work_dir/app-src/auction/xmpp-integration-tests/build/install/auction-xmpp-integration-tests/lib/internal ./internal
COPY --from=checker --chown=$username $work_dir/app-src/auction/xmpp-integration-tests/build/install/auction-xmpp-integration-tests/lib/auction-xmpp-integration-tests.jar .

ENTRYPOINT ["java", "-jar", "--illegal-access=deny", "-ea", "auction-xmpp-integration-tests.jar"]


FROM worker as instrumentedapp
ARG username
ARG work_dir

USER root

RUN apt-get -qq update && \
    DEBIAN_FRONTEND=noninteractive apt-get -qq -o=Dpkg::Use-Pty=0 install \
      curl \
      && rm -rf /var/lib/apt/lists/*

USER $username

# The duplication with app here is necessary to cache the installation of curl in a layer
COPY --from=checker --chown=$username $work_dir/build/goos/lib/external ./external
COPY --from=checker --chown=$username $work_dir/build/goos/lib/agents ./agents
COPY --from=checker --chown=$username $work_dir/build/goos/lib/internal ./internal
COPY --from=checker --chown=$username $work_dir/build/goos/lib/goos.jar .

EXPOSE 1234

ENTRYPOINT ["simple-xvfb-run", "java", "-javaagent:agents/marathon-java-agent.jar=1234", "-Xshare:off", "--illegal-access=deny", "--add-exports", "java.desktop/sun.awt=ALL-UNNAMED", "-jar", "goos.jar"]

COPY --chown=$username scripts/app-running.sh $work_dir/app-running.sh

HEALTHCHECK --interval=1s --retries=20 --timeout=5s CMD ./app-running.sh


FROM worker as app
ARG username
ARG work_dir

# By coping across 3rd party dependencies in a separate step we allow caching of that layer, which
# should be much less changeable than the jars we build
COPY --from=checker --chown=$username $work_dir/build/goos/lib/external ./external
COPY --from=checker --chown=$username $work_dir/build/goos/lib/internal ./internal
COPY --from=checker --chown=$username $work_dir/build/goos/lib/goos.jar .

ENTRYPOINT ["simple-xvfb-run", "java", "--illegal-access=deny", "-jar", "goos.jar"]
