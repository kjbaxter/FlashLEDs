

import asyncio



###############################################################################

async def bar(x):
    count = 0
    while True:
        count += 1
        print('Instance: {} count: {}'.format(x, count))
        await asyncio.sleep(1)  # Pause 1s

###############################################################################


###############################################################################

async def main():
    for x in range(3):
        asyncio.create_task(bar(x))  # No reference stored
    print('Tasks are running')
    await asyncio.sleep(10)

###############################################################################


print('Start')
loop = asyncio.get_event_loop()
#loop.run_until_complete(main())
print('Stop')