## supervisrod 配置文件目录


- start server

`supervisord -c conf/supervisord.conf`

- terminal

```
$ supervisorctl
celery-worker                    RUNNING   pid 34899, uptime 0:01:42
supervisor> help

default commands (type help <topic>):
=====================================
add    exit      open  reload  restart   start   tail   
avail  fg        pid   remove  shutdown  status  update 
clear  maintail  quit  reread  signal    stop    version

supervisor> version
4.0.4
supervisor> 
```

- web

![](https://i.loli.net/2019/08/04/nLZKDV1jz5BPvYQ.png)

- 通过设置 priority 并无法解决 worker 进程启动完毕之后再启动 flower 的样子

priority 只是定义了启动顺序。

http://supervisord.org/configuration.html

https://github.com/Supervisor/supervisor/issues/122​


可以通过设置 `celery-flower` 的 `autostart=true` 为 `autostart=false` 然后再手动进行启动

```
$ supervisorctl       
celery-beat                      STARTING  
celery-flower                    STOPPED   Not started
celery-worker                    STARTING  
supervisor> help

default commands (type help <topic>):
=====================================
add    exit      open  reload  restart   start   tail   
avail  fg        pid   remove  shutdown  status  update 
clear  maintail  quit  reread  signal    stop    version

supervisor> status
celery-beat                      RUNNING   pid 37555, uptime 0:00:17
celery-flower                    STOPPED   Not started
celery-worker                    RUNNING   pid 37556, uptime 0:00:17
supervisor> start celery-flower 
celery-flower: started
supervisor> status
celery-beat                      RUNNING   pid 37555, uptime 0:00:41
celery-flower                    RUNNING   pid 37611, uptime 0:00:15
celery-worker                    RUNNING   pid 37556, uptime 0:00:41
supervisor> 
```

或者使用一个脚本监听 `celery-worker` 的 `status` 进行判断 如果是 `RUNNING` 则可以进行启动 `celery-flower`

```
$ supervisorctl status celery-worker | awk '{print $2}'
RUNNING
```


## qa

- `startsecs`

这个选项是子进程启动多少秒之后，此时状态如果是running，则我们认为启动成功了默认值为 1 非必须设置

- `stopwaitsecs`

这个是当我们向子进程发送 stopsignal 信号后，到系统返回信息给 supervisord，所等待的最大时间。 超过这个时间，supervisord 会向该子进程发送一个强制 kill 的信号。默认为 10 秒 非必须设置

- `priority`

子进程启动关闭优先级，优先级低的，最先启动，关闭的时候最后关闭默认值为 999 非必须设置

## 0x0F

- https://www.cnblogs.com/kevingrace/p/7525200.html