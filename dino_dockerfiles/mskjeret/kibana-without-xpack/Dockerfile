FROM docker.elastic.co/kibana/kibana:6.1.1
ADD kibana.yml /usr/share/kibana/config/

RUN bin/kibana-plugin remove x-pack && kibana 2>&1 | grep -m 1 "Optimization of .* complete" # [1]
