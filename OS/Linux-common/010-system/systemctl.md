## systemctl命令&
说明：向系统管理器查询或发送控制命令

### 用法
```
systemctl [OPTIONS...] {COMMAND} ...
```

| 选项 | 说明
| --- | ---
| --now     | 在启用或禁用unit后，同时启动或停止unit

### COMMAND
| Unit Commands | 说明
| --- | ---
| status [PATTERN...\|PID...]         | 查看运行状态
| start UNIT...                       | 启动服务
| stop UNIT...                        | 停止服务
| reload UNIT...                      | 重载服务
| restart UNIT...                     | 重启服务
| is-active PATTERN...                | 检查是否为活跃状态，退出状态返回0或1
| is-failed PATTERN...                | 检查是否为失败状态，退出状态返回0或1
| list-units [PATTERN...]             | 列出unit
| cat PATTERN...                      | 查看unit文件内容
| list-sockets [PATTERN...]           |
| list-timers [PATTERN...]            |
| show [PATTERN...\|JOB...]           |
| help PATTERN...\|PID...             |
| list-dependencies [UNIT...]         |
| try-restart UNIT...                 |
| reload-or-restart UNIT...           |
| try-reload-or-restart UNIT...       |
| isolate UNIT                        |
| kill UNIT...                        |
| clean UNIT...                       |
| freeze PATTERN...                   |
| thaw PATTERN...                     |
| set-property UNIT PROPERTY=VALUE... |
| bind UNIT PATH [PATH]               |
| mount-image UNIT PATH [PATH [OPTS]] |
| service-log-level SERVICE [LEVEL]   |
| service-log-target SERVICE [TARGET] |
| reset-failed [PATTERN...]           |

| Unit File Commands | 说明
| --- | ---
| enable [UNIT...\|PATH...]           | 设置开机自启
| disable UNIT...                     | 禁用开机自启
| is-enabled UNIT...                  | 检查是否为开机自启状态，退出状态返回0或1
| list-unit-files [PATTERN...]        |
| reenable UNIT...                    |
| preset UNIT...                      |
| preset-all                          |
| mask UNIT...                        |
| unmask UNIT...                      |
| link PATH...                        |
| revert UNIT...                      |
| add-wants TARGET UNIT...            |
| add-requires TARGET UNIT...         |
| edit UNIT...                        |
| get-default                         |
| set-default TARGET                  |

| Machine Commands | 说明
| --- | ---
| list-machines [PATTERN...]          |

| Job Commands | 说明
| --- | ---
| list-jobs [PATTERN...]              |
| cancel [JOB...]                     |

| Environment Commands | 说明
| --- | ---
| show-environment                    |
| set-environment VARIABLE=VALUE...   |
| unset-environment VARIABLE...       |
| import-environment VARIABLE...      |

| Manager State Commands | 说明
| --- | ---
| daemon-reload                       |
| daemon-reexec                       |
| log-level [LEVEL]                   |
| log-target [TARGET]                 |
| service-watchdogs [BOOL]            |

| System Commands | 说明
| --- | ---
| is-system-running                   |
| default                             |
| rescue                              |
| emergency                           |
| halt                                |
| poweroff                            |
| reboot                              |
| kexec                               |
| exit [EXIT_CODE]                    |
| switch-root ROOT [INIT]             |
| suspend                             |
| hibernate                           |
| hybrid-sleep                        |
| suspend-then-hibernate              |


### 示例
```sh
# 显示units运行状态
systemctl status network

# 在禁用时一并停止服务
systemctl disable --now firewalld

# 设置为开机自启，并立即启动
systemctl enable --now dockerd

# 重启network服务
systemctl restart network

# 检查是否为活跃状态，退出状态返回0或1
systemctl is-active network

# 检查是否为失败状态，退出状态返回0或1
systemctl is-failed network

# 检查是否为开机自启状态，退出状态返回0或1
systemctl is-enabled network
```
