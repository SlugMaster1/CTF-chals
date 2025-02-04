# sudo docker build -t math_playground .
# sudo docker run -d -p 1024:1024 --rm -it math_playground

FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc gcc-multilib \
    libc6-dev \
    make \
    gdb \
    # Clean up to reduce the image size
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY math_playground .
COPY flag.txt .
COPY ynetd .

RUN chown -R root:root /home/ctf
RUN chmod 755 /home/ctf /home/ctf/math_playground /home/ctf/ynetd 
RUN chmod 744 /home/ctf/flag.txt

USER ctf
EXPOSE {{challenge.port}}
CMD ./ynetd -p {{challenge.port}} ./math_playground
