FROM docker.elastic.co/kibana/kibana:6.6.0

# Workaround https://github.com/elastic/kibana/issues/10724 and https://github.com/elastic/kibana/issues/6057
RUN XPACK_SECURITY_ENABLED=false /usr/local/bin/kibana-docker 2>&1 | grep -m 1 "Optimization of .* complete in .* seconds"