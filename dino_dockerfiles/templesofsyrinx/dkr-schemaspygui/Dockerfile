
FROM templesofsyrinx/dkr-schemaspy:1.0.0-rc1

LABEL maintainer="Temples of Syrinx (John Chambers-Malewig)"

COPY schemaSpyGUI/ /home/schemaSpy/schemaSpyGUI/

ENTRYPOINT [ "java", "-Djava.ext.dirs=/home/schemaSpy/schemaSpyGUI/lib", "-jar", "/home/schemaSpy/schemaSpyGUI/schemaSpyGUI.jar" ]
