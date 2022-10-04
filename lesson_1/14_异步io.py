"""
协程, 简单的理解，在一子程序内部可以中断(如睡眠、读取文件、io读写等有可能长时间的操作)，然后转而执行其他子程序
关键字: await, async
"""

import asyncio
from time import sleep

def A():
    print("===同步 a1===")
    sleep(3)
    print("===同步 a2===")
    sleep(3)
    print("===同步 a3===")

def B():
    print("===同步 b1===")
    sleep(1)
    print("===同步 b2===")
    sleep(1)
    print("===同步 b3===")

def Sync():
    '''同步执行A、B函数, B函数必须等A执行完毕才开始'''
    A()
    B()

async def AsyncA():
    print("===异步 a1===")
    await asyncio.sleep(3) #await, 让出资源，转而执行其它操作
    print("===异步 a2===")
    await asyncio.sleep(3)
    print("===异步 a3===")

async def AsyncB():
    print("===异步 b1===")
    await asyncio.sleep(1) #await, 让出资源，转而执行其它操作
    print("===异步 b2===")
    await asyncio.sleep(2)
    print("===异步 b3===")

def Async():
    '''异步执行函数A、B'''
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    task = [AsyncA(), AsyncB()]
    loop.run_until_complete(asyncio.wait(task))
    loop.close()


if __name__ == '__main__':
    # 同步例子，a、b不按顺序输出
    Sync()

    # 异步例子，a、b按顺序输出
    Async() 