FROM sh-heating-os:latest
COPY . /usr/local/sh-heating 
COPY bluez /usr/local/bluez
WORKDIR /usr/local/sh-heating
VOLUME ["/usr/local/sh-heating/state"]
CMD php ./daemon/heating_control.php 
