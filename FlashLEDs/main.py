import uasyncio as asyncio
 
async def hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")
 
async def main():
    task = asyncio.create_task(hello())
    await task