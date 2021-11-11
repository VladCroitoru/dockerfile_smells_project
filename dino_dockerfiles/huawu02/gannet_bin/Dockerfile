# huawu02/Gannet2.1
# (https://github.com/huawu02/Gannet2.1/tree/CNI
#  Forked from markmikkelsen/Gannet2.1)
#
# For data collected using the MEGA-PRESS sequence of CNI.
# First build the Matlab Runtime standalone application,
# then run in command-line:
#
# docker build --no-cache -t huawu02/gannet:v2.1 .
#

# Start with the Matlab r2015b runtime container
FROM vistalab/mcr-v90

# Copy shell script and MCR binary to /bin
COPY run_Gannet.sh /bin/run_Gannet
#COPY Gannet_v21 /bin/GannetRun
COPY GannetRun /bin/GannetRun

# change permissions 
RUN chmod +rx /bin/run_Gannet
RUN chmod +x  /bin/GannetRun
