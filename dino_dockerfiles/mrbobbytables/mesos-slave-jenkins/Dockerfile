################################################################################
# mesos-slave-jenkins:1.1.5
# Date: 1/21/2016
# Docker Version: 1.9.1~trusty
# Mesos Version: 0.26.0-0.2.145.ubuntu1404
#
# Description:
# Mesos Slave container with jenkins user added.
################################################################################

FROM mrbobbytables/mesos-slave:1.2.0

MAINTAINER Bob Killen / killen.bob@gmail.com / @mrbobbytables


RUN addgroup --quiet            \
    --system                    \
    --gid 989                   \ 
    jenkins                     \
 && adduser --quiet             \
    --system                    \
    --no-create-home            \
    --ingroup jenkins           \
    --disabled-password         \
    --uid 989                   \
    --shell /bin/bash jenkins 

CMD ["./init.sh"]  
