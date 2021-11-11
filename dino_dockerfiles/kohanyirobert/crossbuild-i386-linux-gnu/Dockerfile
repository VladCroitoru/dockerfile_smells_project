FROM buildpack-deps:wily-scm

RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  cmake \
  g++-multilib \
  gcc-multilib \
  vim-tiny \
  && rm -rf /var/lib/apt/lists/*

ENV HOST_TRIPLE=x86_64-linux-gnu
ENV TARGET_TRIPLE=i386-linux-gnu

ENV PATH=/usr/${TARGET_TRIPLE}/bin:${PATH}
ENV LD_LIBRARY_PATH=/usr/${TARGET_TRIPLE}/lib:${LD_LIBRARY_PATH:-/usr/lib}

RUN mkdir -p /usr/${TARGET_TRIPLE}/bin && \
  ln -s /usr/lib /usr/${TARGET_TRIPLE}/lib && \
  for host_binpath in /usr/bin/${HOST_TRIPLE}-*; \
  do \
    stripped_binname=$(basename ${host_binpath} | sed "s,${HOST_TRIPLE}-,,") && \
    target_binpath=/usr/${TARGET_TRIPLE}/bin/${stripped_binname} && \
    echo ${stripped_binname} | grep -Pq '^(cc|c\+\+(filt)?|gcc|cpp|g\+\+)(-[.0-9]+)?$'; \
    if [ $? -eq 0 ]; \
    then \
      echo "#! /bin/bash\nexec ${host_binpath} -m32 \"\$@\"" > ${target_binpath} && \
      chmod +x ${target_binpath}; \
    else \
      ln -s ${host_binpath} ${target_binpath}; \
    fi; \
  done && \
  ln -s /usr/${TARGET_TRIPLE}/bin/gcc /usr/${TARGET_TRIPLE}/bin/cc && \
  ln -s /usr/${TARGET_TRIPLE}/bin/g++ /usr/${TARGET_TRIPLE}/bin/c++
