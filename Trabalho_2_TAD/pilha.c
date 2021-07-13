/*Bruno Abtibol, Daniel Huf e João Pedro Cunha*/

#include <stdlib.h>
#include <stdio.h>
#include "lista.h"
#include "pilha.h"

struct pilha {
    Lista* lst;
};

Pilha *pilha_cria(void) {
    Lista *l = lst_cria();
    Pilha *p = (Pilha*)malloc(sizeof(Pilha));
    if (p == NULL) {
	    printf("Memoria insuficiente.\n");
		exit(1);
    }
    p->lst = l;
}

int pilha_vazia(Pilha *p) {
    return (lst_vazia(p->lst));
}

void pilha_push(Pilha *p, void *v) {
    lst_insFin(p->lst, v);
}

void *pilha_pop(Pilha *p) {
    void *ret = lst_retFin(p->lst);
    return ret;
}

void pilha_libera(Pilha *p) {
    lst_libera(p->lst);
    free(p);
}