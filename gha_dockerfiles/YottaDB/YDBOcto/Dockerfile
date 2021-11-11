#################################################################
#								#
# Copyright (c) 2019-2020 YottaDB LLC and/or its subsidiaries.	#
# All rights reserved.						#
#								#
#	This source code contains the intellectual property	#
#	of its copyright holder(s), and is made available	#
#	under a license.  If you do not know the terms of	#
#	the license, please stop and do not read further.	#
#								#
#################################################################

FROM yottadb/yottadb-base:latest-master

RUN export DEBIAN_FRONTEND=noninteractive
# `apt-get update` is included to account for the case when the upstream Ubuntu container
# goes out of sync with the upstream Ubuntu repositories. When this happens, `apt-get install`
# fails, causing `docker build` to fail in turn.
RUN apt-get update && \
	apt-get install -y -qq --no-install-recommends \
        git \
        libreadline-dev \
        libconfig-dev \
		cmake

# Copy requisite files from testing environment into Docker build environment
ADD ./build/yottadb_octo* /tmp/build/
ADD ./tools/entrypoint.sh /
# Install from tarball, then use Docker-specific script to include YDBPosix and setup dummy database
RUN cd /tmp/build/ && . /opt/yottadb/current/ydb_env_set && ./octoinstall.sh && ./docker-install.sh
RUN cd /tmp && rm -r build

ENTRYPOINT "/entrypoint.sh"
