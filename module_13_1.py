import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for el in range(1, 6):
        await asyncio.sleep(power)
        print(f'Силач {name} поднял {el} шар')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    print('Старт соревнований')
    strongman1 = asyncio.create_task(start_strongman('3loychel', 3))
    strongman2 = asyncio.create_task(start_strongman('смэрть', 4))
    strongman3 = asyncio.create_task(start_strongman('spectreal', 5))
    await strongman1
    await strongman2
    await strongman3
    print('Финиш соревнований')


asyncio.run(start_tournament())
