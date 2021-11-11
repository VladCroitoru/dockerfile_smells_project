FROM scratch
LABEL maintainer "git[at]frezbo[dot]com"
LABEL com.frezbo.build-date = "__BUILD_DATE__" \
	com.frezbo.description = "Smallest Docker binary" \
	com.frezbo.usage = "https://github.com/frezbo/groot/blob/master/README.md" \
	com.frezbo.url = "frezbo.com" \
	com.frezbo.vcs-url = "https://github.com/frezbo/groot.git" \
	com.frezbo.vcs-ref = "__GIT_SHA__" \
	com.frezbo.version = "__GIT_TAG__" \
	com.frezbo.schema-version = "1.0" \
	com.frezbo.docker.cmd = "docker run --rm frezbo/groot:latest"
COPY ["./groot", "/"]
CMD ["/groot"]

