# collision

![](http://pwnable.kr/img/collision.png)

# Problem

> Daddy told me about cool MD5 hash collision today.
> I wanna do something like that too!
> 
> ssh col@pwnable.kr -p2222 (pw:guest)

# Play

```
col@ubuntu:~$ ls -l
total 16
-r-sr-x--- 1 col_pwn col     7341 Jun 11  2014 col
-rw-r--r-- 1 root    root     555 Jun 12  2014 col.c
-r--r----- 1 col_pwn col_pwn   52 Jun 11  2014 flag
col@ubuntu:~$ cat -n col.c
     1  #include <stdio.h>
     2  #include <string.h>
     3  unsigned long hashcode = 0x21DD09EC;
     4  unsigned long check_password(const char* p){
     5          int* ip = (int*)p;
     6          int i;
     7          int res=0;
     8          for(i=0; i<5; i++){
     9                  res += ip[i];
    10          }
    11          return res;
    12  }
    13
    14  int main(int argc, char* argv[]){
    15          if(argc<2){
    16                  printf("usage : %s [passcode]\n", argv[0]);
    17                  return 0;
    18          }
    19          if(strlen(argv[1]) != 20){
    20                  printf("passcode length should be 20 bytes\n");
    21                  return 0;
    22          }
    23
    24          if(hashcode == check_password( argv[1] )){
    25                  system("/bin/cat flag");
    26                  return 0;
    27          }
    28          else
    29                  printf("wrong passcode.\n");
    30          return 0;
    31  }
```

- line 5 retranslate the char array as int array
- little endian, char 'abcd' => int dbca
- 20 bytes array translates to 20/4=5 32bit integers
- line 19 length check, do not add `\0` in `argv[1]`, here I choose `\x01` for padding

```
col@ubuntu:~$ ./col `python -c "print '\x01'*16+'\xe8\x05\xd9\x1d'"`
daddy! I just managed to create a hash collision :)
```

# Flag

```
daddy! I just managed to create a hash collision :)
```
