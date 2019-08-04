# celery notes

## 使用场景

- 异步任务：将耗时操作任务提交给 celery 去异步执行，比如发送短信/邮件、消息推送、音视频处理等等
- 定时任务：类似于 linux crontab，比如每日数据统计

## 开发

- 启动 flower

`python manage.py celery flower`

可以通过 `--basic_auth=username:password` 添加认证

- 启动 worker

`pipenv run python manage.py celery worker -l INFO`

- 启动 beat

`pipenv run python manage.py celery beat -l INFO`

## supervisor

使用 supervisor 进行进程管理

- 默认配置文件导入

```sh
mkdir conf
echo_supervisord_conf > conf/supervisord.conf
```

- 取消部分注释

```
[inet_http_server]         ; inet (TCP) server disabled by default
port=127.0.0.1:9001        ; ip_address:port specifier, *:port for all iface
[supervisorctl]
serverurl=unix:///tmp/supervisor.sock ; use a unix:// URL  for a unix socket
serverurl=http://127.0.0.1:9001 ; use an http:// url to specify an inet socket
[include]
files = *.ini
```

## qa

- `TypeError: can only concatenate list (not "tuple") to list`

```
  File "/Users/ronething/.local/share/virtualenvs/celeryDEMO-YQTcXGNv/lib/python3.7/site-packages/djcelery/management/commands/celery.py", line 11, in <module>
    class Command(CeleryCommand):
  File "/Users/ronething/.local/share/virtualenvs/celeryDEMO-YQTcXGNv/lib/python3.7/site-packages/djcelery/management/commands/celery.py", line 23, in Command
    preload_options)
TypeError: can only concatenate list (not "tuple") to list
```

django-celery 问题

```
vim /Users/ronething/.local/share/virtualenvs/celeryDEMO-YQTcXGNv/lib/python3.7/site-packages/djcelery/management/commands/celery.py
```

将一下这几行注释

```
   21     # options = (cc_options +                                                                                            
   22     #            base_options +                                                                                          
   23     #            preload_options) 
```

- `kombu.async.timer`

```
  File "/Users/ronething/.local/share/virtualenvs/celeryDEMO-YQTcXGNv/lib/python3.7/site-packages/celery/utils/timer2.py", line 19
    from kombu.async.timer import Entry, Timer as Schedule, to_timestamp, logger
                   ^
SyntaxError: invalid syntax
```

解决方法：async 在 python3.7 已经是关键字 降级或者改变量名

- `pipenv.patched.notpip._internal.exceptions.InstallationError` 

```
pipenv.patched.notpip._internal.exceptions.InstallationError: Command "python setup.py egg_info" failed with error code 1 in /var/folders/xr/8kys7jh56tn91lhc_72nh_wh0000gn/T/tmp1morwpx6build/lazy-object-proxy/
```


解决方法：`export AIRFLOW_GPL_UNIDECODE=yes` 刚好适用我 如果出现其他情况，请另寻解决方案

https://github.com/pypa/pipenv/issues/2791#issuecomment-420948394

- tasks 实例化过程

https://blog.csdn.net/qq_40394962/article/details/85495285

## 0x0F

- http://www.beixiongxiong.com/course/10103254/2123/
- https://www.cnblogs.com/cwp-bg/p/10575688.html
