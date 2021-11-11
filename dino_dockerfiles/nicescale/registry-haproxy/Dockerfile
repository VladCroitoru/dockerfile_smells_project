from registry:latest
run apt-get -y install haproxy
run sed -i 's/^ENABLED.*/ENABLED=1/' /etc/default/haproxy
add haproxy.cfg /etc/haproxy/haproxy.cfg
expose 8088 5000
cmd /etc/init.d/haproxy start && exec docker-registry
