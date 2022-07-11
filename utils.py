from statistics import mean
from tabulate import tabulate
from time import time


def make_table(results: dict[int, list]):
    # Adiciona a média de cada categoria
    for valores_cat in zip(*results.values()):
        media_valores_cat = mean(valores_cat)

        results.setdefault("Média", []).append(media_valores_cat)

    # Adiciona a média de cada sample size
    for values in results.values():
        values.append(mean(values))

    print(
        tabulate(
            {" ": ["Categoria 1", "Categoria 2", "Categoria 3", "Média"]} | results,
            headers="keys",
            numalign="center",
            tablefmt="fancy_grid",
        )
    )


def fazer_testes(funcao, repeticoes, sizes=[100, 200, 500, 1000, 2000, 5000, 10000]):
    res = {}
    tempos = {}

    for i in range(repeticoes):
        for cat in [1, 2, 3]:
            for size in sizes:
                start = time()
                desempenho = funcao(cat, size)
                end = time()

                if i == 0:
                    res.setdefault(size, []).append(desempenho)

                # Guarda o tempo de execução dos 3 maiores sample sizes para cada categoria
                if size in sizes[::-1][:3]:
                    t = end - start

                    tempos.setdefault(size, [0, 0, 0])
                    tempos[size][cat - 1] = t

    for ts in tempos.values():
        for t in ts:
            t = t / repeticoes

    return res, tempos
