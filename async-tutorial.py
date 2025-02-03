import asyncio

async def display():
    await print(' I am running display******')

async def count():
    print("one")
    await asyncio.sleep(1)
    print('After Awaiting****')
    


asyncio.run(count())