import asyncio

delay = 10
count = 5
names = {'Василий': 2, 'Петр': 3, 'Иван': 4}
tasks = []

async def start_strongman(name, power):
  suffix = ''
  print(f'Силач {name} начал соревнования.')
  for i in range(1, count + 1):
    await asyncio.sleep(delay/power)
    if i == 2 or i == 3 or i == 4:
      suffix = 'а'
    elif i == 5:
      suffix = 'ов'
    print(f'Силач {name} поднял {i} шар{suffix}')
  print(f'Силач {name} закончил соревнования.')

async def start_tournament():
  for i in range(len(names)):
    tasks.append(asyncio.create_task(start_strongman(list(names)[i], names[list(names)[i]])))
  for i in range(len(names)):
    await tasks[i]


asyncio.run(start_tournament())
