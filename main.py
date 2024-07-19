import random
import threading
import time
import matplotlib.pyplot as plt

def split_arr(arr, divisions):
    return [arr[i:i + divisions] for i in range(0, len(arr), divisions) if len(arr[i:i + divisions]) > 0]

def parallel_sumup(arr, threads_count):
    splitted_arr = split_arr(arr, len(arr) // threads_count)
    threads_sum_list = list()

    def sumup(arr):
        threads_sum_list.append(sum(arr))

    thread_list = list()
    for t in range(threads_count):
        th = threading.Thread(target=sumup, args=(splitted_arr[t],))
        thread_list.append(th)
        th.start()
        
    for th in thread_list:
        th.join()
        
    return sum(threads_sum_list)

def sequential_sumup(arr):
    print("\nSomando elementos do array sequencialmente...")
    return sum(arr)

def randomizer(arr_size):
    print("\nGerando array aleatório...")
    return [random.randint(1, 100) for _ in range(arr_size)]

arr_size = int(input("Digite o tamanho do vetor: "))
max_threads = int(input("Digite a quantidade de threads: "))

rand_arr = randomizer(arr_size)

seq_start_time = time.time()
seq_sum = sequential_sumup(rand_arr)
seq_sumup_time = time.time() - seq_start_time
print(f"Tempo de execução sequencial: {seq_sumup_time:.6f} segundos")

paral_times = list()
thread_counts = list(range(1, max_threads + 1))


print("\nIniciando soma paralela...")
for t in thread_counts:
    paral_start_time = time.time()
    par_sum = parallel_sumup(rand_arr, t)
    paral_sump_time = time.time() - paral_start_time
    print(f"Tempo de execução com {t} threads: {paral_sump_time:.6f} segundos")
    paral_times.append(paral_sump_time)

plt.figure(figsize=(10, 6))
plt.plot(thread_counts, paral_times, label='Paralelo')
plt.axhline(y=seq_sumup_time, color='r', linestyle='-', label='Sequencial')
plt.xlabel('Quantidade de threads')
plt.ylabel('Tempo de execução (segundos)')
plt.title('Tempo de execução vs. Quantidade de threads')
plt.legend()
plt.show()
