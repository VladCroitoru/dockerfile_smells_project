ARG PAYARA_VERSION=latest

FROM payara/micro:${PAYARA_VERSION}

# copy required files
# we also setup the command files, so it is more easy to override and have the runtime arguments set by default
COPY payara-config.properties \
    run_payara.sh \
    logging-json.properties logging-plain.properties \
    post-boot-commands.txt post-deploy-commands.txt pre-boot-commands.txt \
    ${PAYARA_PATH}/

# switch to root temporarily as we need more rights for the following chown
USER root

# extract the truststore so it is more easy to add own certificates. Also create a keystore file
# create libs directory so we can use --addlibs without payara complaining
# set ownership allow access with group root, which is required for openshift
RUN jar xf payara-micro.jar MICRO-INF/domain/cacerts.jks MICRO-INF/domain/keystore.jks \
    && mv MICRO-INF/domain/cacerts.jks . \
    && mv MICRO-INF/domain/keystore.jks . \
    && mkdir libs \
    && chmod 755 run_payara.sh \
    && chown -R payara:root /opt/payara \
    && chmod g+w /opt/payara

USER payara

# set this logging-plain.properties to get more readable log files for debugging
ENV LOG_PROPERTIES_FILE=logging-json.properties

# control deployment options, which is used in the run_payara.sh script either to have --deploy or --deploydir
ENV DEPLOYDIR=/opt/payara/deployments
ENV DEPLOY=""

# use script as entrypoint so we can use environment variables
ENTRYPOINT ["/opt/payara/run_payara.sh"]

# apply common arguments. Left in cmd and not put to above entry point to make it more easy to override them
CMD ["--systemproperties", "payara-config.properties", \
    "--postbootcommandfile", "post-boot-commands.txt", \
    "--postdeploycommandfile", "post-deploy-commands.txt", \
    "--prebootcommandfile", "pre-boot-commands.txt", \
    "--addlibs", "libs" ]

# use trust and keystores
# also set some basic java tuning parameters for huge machines
ENV JAVA_BASE_OPTIONS="\
-Djavax.net.ssl.trustStore=cacerts.jks \
-Djavax.net.ssl.keyStore=keystore.jks \
-server \
-Djava.awt.headless=true \
-XX:NewRatio=5 \
-XX:+DisableExplicitGC \
-XX:ParallelGCThreads=2 \
-XX:CICompilerCount=2"

# set some sane basic java memory settings. Separated in order to allow easy override of these only
ENV JAVA_MEMORY_OPTIONS="\
-XX:MaxMetaspaceSize=256m \
-Xmx512m \
-Xms256m \
-Xss256k"
