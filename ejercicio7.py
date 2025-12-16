import time, random, asyncio, threading, multiprocessing

def consultar_db(nombre):
    t = random.uniform(1, 5)
    time.sleep(t)
    return f"OK {nombre} en {t:.2f}s"

def consultas_hilos():
    resultados = []
    def tarea(idx):
        resultados.append(consultar_db(f"consulta_hilo_{idx}"))

    inicio = time.time()
    hilos = [threading.Thread(target=tarea, args=(i,)) for i in range(1, 4)]
    for h in hilos: h.start()
    for h in hilos: h.join()
    fin = time.time()
    return fin - inicio, resultados

async def consultar_db_async(nombre):
    t = random.uniform(1, 5)
    await asyncio.sleep(t)
    return f"OK {nombre} en {t:.2f}s"

async def consultas_async():
    inicio = time.time()
    tareas = [consultar_db_async(f"consulta_async_{i}") for i in range(1, 4)]
    resultados = await asyncio.gather(*tareas)
    fin = time.time()
    return fin - inicio, resultados

def consultas_procesos():
    inicio = time.time()
    with multiprocessing.Pool(processes=3) as pool:
        resultados = pool.map(consultar_db, [f"consulta_proceso_{i}" for i in range(1, 4)])
    fin = time.time()
    return fin - inicio, resultados

if __name__ == "__main__":
    t_h, r_h = consultas_hilos()
    t_a, r_a = asyncio.run(consultas_async())
    t_p, r_p = consultas_procesos()

    print(f"Hilos: {t_h:.2f}s -> {r_h}")
    print(f"Asincronia: {t_a:.2f}s -> {r_a}")
    print(f"Procesos: {t_p:.2f}s -> {r_p}")

    tiempos = {"Hilos": t_h, "Asincronia": t_a, "Procesos": t_p}
    mas_rapido = min(tiempos, key=tiempos.get)
    mas_lento = max(tiempos, key=tiempos.get)

    print(f"Mas rapido: {mas_rapido}")
    print(f"Mas lento: {mas_lento}")
    print("Explicacion:")
    print("- Hilos: varios hilos en el mismo proceso.")
    print("- Asincronia: corutinas (async/await) organizan tareas cooperativamente.")
    print("- Procesos: interpretes y memoria independientes.")


