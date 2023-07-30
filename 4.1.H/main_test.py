import asyncio
import sys
import time


async def get_number(name):
    print(f"開始看診{name}")
    # await asyncio.sleep(2)
    time.sleep(2)
    print("看完了")

lista = []
tasks = []
async def check():
    while True:
        name = input("姓名：")
        lista.append(name)
        tasks.append(get_number(lista.pop(0)))
        await asyncio.gather(*tasks)



import asyncio
from concurrent.futures import ThreadPoolExecutor


async def ainput(prompt: str = "") -> str:
    with ThreadPoolExecutor(1, "AsyncInput") as executor:
        return await asyncio.get_event_loop().run_in_executor(executor, input, prompt)


async def main():
    name = await ainput("What's your name? ")
    print(f"Hello, {name}!")




if __name__ == '__main__':
    asyncio.run(main())


