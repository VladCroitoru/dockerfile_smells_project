from ubuntu:12.04
run apt-get install -y python
expose 8000
cmd python -m SimpleHTTPServer
workdir /home/browse/www
ADD build /usr/local/bin/
# End of base image
ADD . /home/browse/src/
RUN build /home/browse/src/ /home/browse/www/
