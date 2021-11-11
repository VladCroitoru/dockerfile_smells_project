FROM zoobab/lede-17.01.0-rc2-r3131-42f3c1f-x86-64
RUN opkg update
RUN opkg install babeld
ENTRYPOINT ["babeld","-d","9","eth0"]
