FROM frekele/gradle:3.2.1-jdk8
MAINTAINER FlexConstructor <flexconstructor@gmail.com>


#==================================
# Environment variables.
#==================================

ENV FLASH_DIR              /opt/flash/workspace
ENV FLASH_PLAYER_EXE        /usr/bin/gflashplayer
ENV DISPLAY                :99.0
ENV FLASH_PLAYER_LINK      https://fpdownload.macromedia.com/pub/labs/flashruntimes/flashplayer/linux64/flash_player_sa_linux_debug.x86_64.tar.gz


#==================================
# Install Dependencies.
#==================================

# for running standalone debug flashplayer
RUN apt-get update &&   \
	apt-get install -y  \
			libnss3	    \
			libgtk2.0-0 \
			xvfb &&     \
	apt-get clean


#==================================
# Install Debug Flash Player.
#==================================

RUN mkdir -p $FLASH_DIR &&                                              \
    cd $FLASH_DIR &&                                                    \
    curl $FLASH_PLAYER_LINK                                             \
    	--progress-bar                                                  \
    	-o flash_player.tar.gz &&                                       \
    tar xzf flash_player.tar.gz &&                                      \
    rm flash_player.tar.gz &&                                           \
    mkdir -p /usr/lib/flashplayer &&                                    \
    mv flashplayerdebugger /usr/lib/flashplayer/flashplayerdebugger &&  \
    rm -rf /usr/bin/flashplayerdebugger &&                              \
    ln -s /usr/lib/flashplayer/flashplayerdebugger /usr/bin/gflashplayer


#==================================
# Configure run.
#==================================

RUN mkdir -p  ${FLASH_DIR}
VOLUME       ${FLASH_DIR}
WORKDIR ${FLASH_DIR}
ENTRYPOINT xvfb-run -e /dev/stdout --server-args="$DISPLAY -screen 0 830x1200x24 -ac +extension RANDR" $0 $*
