FROM busybox:latest

ADD https://github.com/upfluence/vulcand-auth/releases/download/v0.0.3/vulcand-linux-amd64 /vulcand
RUN chmod +x /vulcand

CMD /vulcand -logSeverity=${LOG_LEVEL:-"WARN"} -etcd="http://172.17.42.1:4001" \
  -sealKey=${SEAL_KEY:-""} -statsdAddr=${STATSD_URL:-""} \
  -statsdPrefix=${STATSD_PREFIX:-""} -etcdKey=${ETCD_KEY:-"vulcand"}
