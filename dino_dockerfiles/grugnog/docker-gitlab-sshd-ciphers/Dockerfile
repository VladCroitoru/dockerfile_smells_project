FROM gitlab/gitlab-ce:9.1.3-ce.0
# Default plus aes256-cbc
RUN echo 'Ciphers chacha20-poly1305@openssh.com,aes128-ctr,aes192-ctr,aes256-ctr,aes128-gcm@openssh.com,aes256-gcm@openssh.com,aes256-cbc' >> /assets/sshd_config
# Default plus diffie-hellman-group-exchange-sha1
RUN echo 'KexAlgorithms curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group14-sha1,diffie-hellman-group-exchange-sha1' >> /assets/sshd_config
