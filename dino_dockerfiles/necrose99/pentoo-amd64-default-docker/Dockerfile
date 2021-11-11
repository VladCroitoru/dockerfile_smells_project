FROM gentoo/stage3-amd64

MAINTAINER necrose99 necrose99@protmail.ch mike@michaellawrenceit.com

RUN echo "Getting power ISO to Unpack Pentoo into the Gentoo root & Overlay"
RUN wget -O poweriso-1.3.tar.gz http://goo.gl/p8Tzc
RUN tar -xzvf poweriso-1.3.tar.gz -C /usr/local/bin
RUN chmod +x /usr/local/bin/poweriso
RUN mkdir /pentoo_tmp
RUN cd  /pentoo_tmp
RUN wget -bqc http://www.pentoo.ch/isos/latest-iso-symlinks/pentoo-amd64-default.iso
RUN echo pentoo-amd64-default.iso unpacking"
RUN emerge -v sys-fs/squashfs-tools app-arch/p7zip
RUN poweriso extract  ~ *.iso / -od ~/pentoo_tmp/ ; exit 0 
  #### if this fails I know 7zip will unpack iso.
RUN 7z x *.iso 
RUN echo "unpacking Squashfile and modules"
RUN unsquashfs -f -d / /pentoo_tmp/image.squashfs
RUN unsquashfs -f -d / /pentoo_tmp/*.lzm 
RUN  rm -rf /pentoo_tmp/  #Cleanup ISLE 5
RUN pentoo-updater  #A. Test to make sure files copied over ,b. update Binaries.
RUN eslect profile set pentoo:pentoo/hardened/linux/amd64/bleeding_edge   #Prep for building newest 
RUN echo "Bootstrapped  Pentoo iso into /: ,ready for builds"
