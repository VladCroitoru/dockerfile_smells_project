FROM techio/sbt:0.13.15

ENV SBT_OPTS="-Xmx768M -XX:+UseConcMarkSweepGC -XX:+CMSClassUnloadingEnabled -Xss2M  -Duser.timezone=GMT"

COPY build.sh      /project/build
COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
