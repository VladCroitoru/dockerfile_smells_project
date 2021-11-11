FROM agustinhenze/zephyr-docker-core

# Building dependencies
RUN apt-get update && apt-get install gcc-arm-none-eabi libnewlib-dev --no-install-recommends -y && rm -rf /var/lib/apt

# Debugging dependencies
RUN apt-get update && eatmydata apt-get install openocd gdb-arm-none-eabi --no-install-recommends -y && rm -rf /var/lib/apt

# Emulation dependencies
RUN apt-get update && eatmydata apt-get install qemu-system-arm --no-install-recommends -y && rm -rf /var/lib/apt

# Programming dependencies
RUN apt-get update && eatmydata apt-get install dfu-util --no-install-recommends -y && rm -rf /var/lib/apt
