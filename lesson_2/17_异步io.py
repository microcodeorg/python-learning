"""
协程, 简单的理解，在一子程序内部可以中断(如睡眠、读取文件、io读写等有可能长时间的操作)，然后转而执行其他子程序
关键字: await, async
"""

import asyncio
from time import sleep


def print_yellow(val):
    print('\x1b[1;33;40m' + val + '\x1b[0m')


def print_green(val):
    print('\033[0;32;40m' + val + '\033[0m')


def func_a():
    print_yellow('===同步 a1===')
    sleep(3)
    print_yellow("===同步 a2===")
    sleep(3)
    print_yellow("===同步 a3===")


def func_b():
    print_green("===同步 b1===")
    sleep(1)
    print_green("===同步 b2===")
    sleep(1)
    print_green("===同步 b3===")


def func_sync():
    """同步执行A、B函数, B函数必须等A执行完毕才开始"""
    func_a()
    func_b()


async def func_async_a():
    print_yellow("===异步 a1===")
    await asyncio.sleep(3)  # await, 让出资源，转而执行其它操作
    print_yellow("===异步 a2===")
    await asyncio.sleep(3)
    print_yellow("===异步 a3===")


async def func_async_b():
    print_green("===异步 b1===")
    await asyncio.sleep(1)  # await, 让出资源，转而执行其它操作
    print_green("===异步 b2===")
    await asyncio.sleep(2)
    print_green("===异步 b3===")


async def func_async():
    """异步执行函数A、B"""
    await asyncio.wait([
        asyncio.create_task(func_async_a()),
        asyncio.create_task(func_async_b()),
    ])


if __name__ == '__main__':
    # 同步例子，a、b不按顺序输出
    print("同步：")
    func_sync()

    print("#" * 50)

    print("异步：")
    # 异步例子，a、b按顺序输出
    # func_async()
    asyncio.run(func_async())
