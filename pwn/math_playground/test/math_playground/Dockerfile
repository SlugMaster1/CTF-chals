# sudo docker build -t math_playground .
# sudo docker run -d -p 1024:1024 --rm -it math_playground

FROM ubuntu:22.04

RUN apt-get update

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
EXPOSE 1024
CMD ./ynetd -p 1024 ./math_playground
