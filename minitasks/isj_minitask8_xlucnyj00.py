# minitask 8
import asyncio
import time

async def perform_task(duration, task_name):
    print(task_name, 'starting')
    await asyncio.sleep(duration)
    print(task_name, 'is done')

async def main():
    boiling_task = asyncio.create_task(perform_task(3, 'boiling kettle'))
    cleaning_task = asyncio.create_task(perform_task(2, 'cleaning cups'))

    await boiling_task
    await cleaning_task

s = time.perf_counter()
asyncio.run(main())
elapsed = time.perf_counter() - s
print(f"Executed in {elapsed:0.2f} seconds.")
