## Windows Terminal输入命令
1. 清空 NodeMCU 的 Flash 存储芯片: 
`esptool.py --chip esp32 --port COM4 erase_flash`

2. 将固件写入 Flash 芯片: 
`esptool.py --chip esp32 --port COM4 --baud 460800 write_flash -z 0x1000 esp32-20220117-v1.18.bin`

3. 上传文件

[ble_advertising.py源文件来源](https://raw.githubusercontent.com/micropython/micropython/master/examples/bluetooth/ble_advertising.py)
```
ampy -p COM4 -b 115200 -d 0.5 put ble_lightsensor.py
ampy -p COM4 -b 115200 -d 0.5 put ble_advertising.py
ampy -p COM4 -b 115200 -d 0.5 put lightsensor.py
ampy -p COM4 -b 115200 -d 0.5 put main.py
```

## 代码勘误
原因: mac获取得到的是一个tuple对象 ex: (0, b'4\\x86]\\xb6\\xeb\\x0e'), 应取第二个值
位置: ble_lightsensor.py中build_mi_sdadv方法下语句`service_data = struct.pack("<3HB",uuid,fc,pid,fcnt)+mac+struct.pack("<H2BH",objid,objlen,0,objval)`
修订: `service_data = struct.pack("<3HB",uuid,fc,pid,fcnt)+mac[1]+struct.pack("<H2BH",objid,objlen,0,objval)`

## 插入代码
1. ble_advertising.py中添加常量`_ADV_TYPE_SERVICE_DATA = const(0x16)`
2. ble_advertising.py的advertising_payload方法参数中添加`service_data = None`, 然后在方法中加入下面语句:
```
if service_data:
    _append(_ADV_TYPE_SERVICE_DATA, service_data)
```

## 参考资料
[micropython文档](https://docs.micropython.org/en/latest/library/os.html)

[python_tuples](https://www.w3schools.com/python/python_tuples.asp)