import asyncio
from asyncio import run


class Processor:
    async def process(timeout):
        # simulate some processing, usually I/O
        await asyncio.sleep(timeout)
        print("done")

    async def process_batch_example(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run(loop))
        loop.close()
        tasks = []
        for x in range(50):
            tasks.append(self.process(x))
        await asyncio.gather(*tasks)
