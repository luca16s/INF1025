def produtoLista (L):
    produto = 1
    for el in L:
        if type(el) in [int,float]:
            produto*=el
        elif type(el) == list:
            tot = produtoLista(el)
            produto*=tot

    return produto

L3 = [3, [98, [2, 1], 10], 30]
produtoLista(L3)
print(produtoLista(L3))
