FROM pshouse/squeak-base 

ENV VERSION 4.5
ENV IMAGEROOT Squeak-$VERSION-All-In-One/Squeak-$VERSION-All-in-One.app
ENV RESOURCES $IMAGEROOT/Contents/Resources/
ADD http://ftp.squeak.org/$VERSION/Squeak-$VERSION-All-in-One.zip Squeak.zip
RUN unzip Squeak.zip

#RUN ln -s $RESOURCES/Squeak4.5-13680.changes /usr/share/nginx/html
#RUN ln -s $RESOURCES/Squeak4.5-13680.image /usr/share/nginx/html
#RUN chmod a+r $RESOURCES/Squeak4.5-13680.changes
#RUN chmod a+r $RESOURCES/Squeak4.5-13680.image

#RUN git clone --depth 1 https://github.com/JumpIntoSqueak/metacello-git.git /metacello-git
#RUN sudo gem install hub

ADD install.st /
RUN $IMAGEROOT/Contents/LinuxAndWindows/Linux-i686/bin/squeak -vm-sound-null -vm-display-null -headless $RESOURCES/Squeak*.image /install.st

ADD run.sh /
ADD _run.st /
