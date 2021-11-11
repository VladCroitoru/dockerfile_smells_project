FROM busybox

MAINTAINER Michal Orzechowski <orzechowski.michal@gmail.com>

ARG PATHS_FILE
ARG NUMBER_OF_FILES
LABEL number-of-files=${NUMBER_OF_FILES}

ENV NUMBER_OF_FILES=${NUMBER_OF_FILES}
ENV DATA_DIR=/data

COPY ${PATHS_FILE} /paths
RUN mkdir $DATA_DIR && while read file ; do file="$DATA_DIR/$file" ; mkdir -p "$(dirname $file)" ; echo "$file" > "$file"  ; done < paths