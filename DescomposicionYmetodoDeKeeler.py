from sympy.combinatorics import Permutation
from sympy.interactive import init_printing
init_printing(perm_cyclic=False, pretty_print=False)

def to_cycles(perm):
    pi = {i+1: perm[i] for i in range(len(perm))}
    cycles = []

    while pi:
        elem0 = next(iter(pi)) # arbitrary starting element
        this_elem = pi[elem0]
        next_item = pi[this_elem]

        cycle = []
        while True:
            cycle.append(this_elem)
            del pi[this_elem]
            this_elem = next_item
            if next_item in pi:
                next_item = pi[next_item]
            else:
                break

        cycles.append(cycle)

    return cycles

def Metodo_Keeler(P):
  alpha,beta = max(P)+1, max(P)+2
  nuevos = Permutation(alpha,beta)
  Intercambio = to_cycles(P)
  l = 0
  while l < len(Intercambio):
    if len(Intercambio[l]) == 1:
      Intercambio.remove(Intercambio[l])
    else:
      l +=1 

  numero_de_ciclos = len(Intercambio)
  permutacion = Permutation(Intercambio)
  sigmas = []

  for i in range(numero_de_ciclos):
    sigma_i = []
    for j in range(len(Intercambio[i])-1):
      sigma_i.append([alpha,Intercambio[i][j]])

    sigma_i.append([beta,Intercambio[i][-1]])
    sigma_i.append([alpha,Intercambio[i][-1]])
    sigma_i.append([beta,Intercambio[i][0]])
    sigmas.append(sigma_i)

  nuevos_sigmas = []
  for ciclos in sigmas:
    ciclos.reverse()
    nuevos_sigmas.append(Permutation(ciclos))
  print(nuevos_sigmas)
  tau = 1
  for sigma_j in reversed(nuevos_sigmas):
    tau = tau*sigma_j
  print("tau: ",tau)
  if numero_de_ciclos % 2 == 0:
    sigma_final = tau
  else:
    sigma_final = nuevos*tau
   
  print(sigma_final*permutacion)



#P = [13,2,15,14,10,6,12,3,4,1,7,9,5,11,8]
P = [13,18,10,15,19,6,4,14,1,12,9,2,5,20,11,7,17,8,16,3]
#P = [4,5,1,3,2]
#P = [1,2,4,3]

print("Descomposición en ciclos disjuntos de P: ",to_cycles(P))


Metodo_Keeler(P)
