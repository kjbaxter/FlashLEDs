import uasyncio as asyncio
 
async def task1():
    for i in range(3):
        print("Task 1:", i)
        await asyncio.sleep(0.5)
 
async def task2():
    for i in range(3):
        print("Task 2:", i)
        await asyncio.sleep(0.3)
 
async def main():
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    await asyncio.gather(t1, t2)
 
asyncio.run(main())