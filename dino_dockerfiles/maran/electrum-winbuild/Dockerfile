FROM ubuntu:14.04
MAINTAINER maran.hidskes@gmail.com

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y software-properties-common && add-apt-repository -y ppa:ubuntu-wine/ppa
RUN dpkg --add-architecture i386
RUN apt-get update -y
RUN apt-get install -y wine1.7 xvfb wget
RUN apt-get install -y winbind

RUN apt-get purge -y python-software-properties
RUN apt-get autoclean -y

# Versions
ENV PYTHON_URL https://www.python.org/ftp/python/2.7.8/python-2.7.8.msi
ENV PYQT4_URL http://downloads.sourceforge.net/project/pyqt/PyQt4/PyQt-4.11.1/PyQt4-4.11.1-gpl-Py2.7-Qt4.8.6-x32.exe?r=http%3A%2F%2Fwww.riverbankcomputing.co.uk%2Fsoftware%2Fpyqt%2Fdownload&ts=1410031650&use_mirror=skylink
ENV PYWIN32_URL http://downloads.sourceforge.net/project/pywin32/pywin32/Build%20217/pywin32-217.win32-py2.7.exe?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fpywin32%2Ffiles%2Fpywin32%2FBuild%2520217%2F&ts=1410031204&use_mirror=kent
ENV PYINSTALLER_URL https://pypi.python.org/packages/source/P/PyInstaller/PyInstaller-2.1.zip
ENV NSIS_URL http://prdownloads.sourceforge.net/nsis/nsis-2.46-setup.exe?download

# Paths
ENV WINEPREFIX /opt/wine-electrum
RUN export WINEPREFIX=/opt/wine-electrum

ENV ELECTRUM_PATH $WINE_PREFIX/drive_c/electrum
ENV PYHOME c:/Python27
ENV PYTHON xvfb-run -a wine $PYHOME/python.exe -B
ENV PIP $PYTHON -m pip

# Only needed for debugging
# RUN apt-get install -y vnc4server
# RUN export DISPLAY=:33
# RUN (echo electrum;echo electrum)|vnc4passwd
# EXPOSE 5933

# Docker kills this run before wine is done setting up, don't remove the sleep
RUN xvfb-run -a --server-num=4 wineboot && sleep 5

# Install stuff
RUN wget -O python.msi "$PYTHON_URL"
RUN xvfb-run -a -e /dev/stdout -a msiexec /q /i python.msi && sleep 5

RUN wget -O pyinstaller.zip "$PYINSTALLER_URL" && unzip pyinstaller.zip && mv PyInstaller-2.1 $WINEPREFIX/drive_c/pyinstaller

RUN wget -O pywin32.exe "$PYWIN32_URL"
RUN unzip -qq pywin32.exe; echo 'Done pywin'
RUN cp -r PLATLIB/* $WINEPREFIX/drive_c/Python27/Lib/site-packages/
RUN mkdir -p $WINEPREFIX/drive_c/Python27/Scripts/
RUN cp -r SCRIPTS/* $WINEPREFIX/drive_c/Python27/Scripts/
RUN $PYTHON $PYHOME/Scripts/pywin32_postinstall.py -install

RUN wget -O PyQt.exe "$PYQT4_URL"
RUN rm -rf /tmp/.wine-* && xvfb-run -a wine PyQt.exe /S

VOLUME ["/opt/wine-electrum/drive_c/electrum"]

RUN wget -q -O nsis.exe $NSIS_URL
RUN rm -rf /tmp/.wine-* && xvfb-run -a wine nsis.exe /S

# Pip not needed for releases
#RUN wget -q -O - https://raw.github.com/pypa/pip/master/contrib/get-pip.py | $PYTHON

ADD ./helpers/build-binary /usr/bin/build-binary

# Clean up stale wine processes
RUN rm -rf /tmp/.wine-*
