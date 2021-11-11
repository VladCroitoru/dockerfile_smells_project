# Use official Ubuntu release
FROM ubuntu:latest

# Update Ubuntu image
RUN apt-get -qq update && apt-get -qq upgrade

# Install CUPS and CUPS-PDF
RUN DEBIAN_FRONTEND=noninteractive TZ=Europe/Berlin apt-get -qq install cups cups-pdf wget unzip

# Clean up updates/install
RUN apt-get -qq autoclean && apt-get -qq autoremove && apt-get -qq clean

# Install DELL driver S282cdn/H825cdn
RUN cd /tmp && \
    wget https://downloads.dell.com/FOLDER03385341M/1/Printer_H825cdw_Driver_Dell_A00_Linux.zip && \
    unzip Printer_H825cdw_Driver_Dell_A00_Linux.zip && \
    dpkg -i S2825cdn-H825cdw/dell-color-mfp-s2825cdn-h825cdw-1.0-3_amd64.deb && \
    cd

# Install Kyocera FS-C5100DN KPDL driver
# See: https://www.openprinting.org/printer/Kyocera/Kyocera-FS-C5100DN_KPDL
RUN mkdir /usr/share/ppd/Kyocera
ADD ppd/Kyocera_FS-C5100DN_KPDL.ppd.gz /usr/share/ppd/Kyocera/Kyocera_FS-C5100DN_KPDL.ppd.gz

# Copy scripts and configurations files into container
ADD start_cups /root/start_cups
ADD cupsd.conf /root/cupsd.conf

# Allow execution of start script
RUN chmod u+x /root/start_cups

# Make CUPS port available
EXPOSE 631

# Export volumes
VOLUME /config

# Start cups
CMD ["/root/start_cups"]

