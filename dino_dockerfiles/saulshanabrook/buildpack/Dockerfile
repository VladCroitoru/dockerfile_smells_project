FROM flynn/cedarish

# from ./flynn/slugbuilder/Dockerfile
ADD ./flynn/slugbuilder/builder /tmp/builder
RUN xargs -L 1 /tmp/builder/install-buildpack /tmp/buildpacks < /tmp/builder/buildpacks.txt

# from ./flynn/slugrunner/Dockerfile
ADD ./flynn/slugrunner/runner /tmp/runner

ADD init_alias.sh /tmp/runner/init_alias.sh

ONBUILD ADD . /tmp/code/
# exporting .env file from http://stackoverflow.com/a/20909045
ONBUILD RUN tar -cC /tmp/code . | env $(cat /tmp/code/build.env | xargs) /tmp/builder/build.sh

ENTRYPOINT ["/tmp/runner/init_alias.sh"]
