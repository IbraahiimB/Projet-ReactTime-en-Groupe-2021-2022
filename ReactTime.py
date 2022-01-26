import time,random

print("Quand le go apparaît, clique vite sur Entrée")
time.sleep(1)
print ('prêt ?')
time.sleep(1)
time.sleep(random.randint(2,7))
print('GO')
tic =  time.perf_counter()
a= input()
tac = time.perf_counter()

temps = tac-tic

print(f"Votre temps est {temps} seconde")
            
