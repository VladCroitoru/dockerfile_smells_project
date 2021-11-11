FROM dt27/domoticz-cn:init
MAINTAINER DT27 <dragonet1943@gmail.com>

EXPOSE 31080 31443

ENTRYPOINT ["/src/domoticz/domoticz", "-www", "31080", "-sslwww" ,"31443", "-dbase", "/src/domoticz/domoticz.db", "-sslcert", "/src/domoticz/server_cert.pem", "-log", "/src/domoticz/domoticz.log"]
