FROM debian:jessie

run echo "deb-src http://ftp.fr.debian.org/debian/ jessie main contrib non-free" > /etc/apt/sources.list.d/deb-src.list
run apt-get update -qy
run apt-get install -y libhiredis-dev coccinelle git clang wget libprelude-dev
run apt-get build-dep -y suricata

