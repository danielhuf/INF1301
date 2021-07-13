/*Bruno Abtibol, Daniel Huf e João Pedro Cunha*/

#include <stdlib.h>
#include <stdio.h>
#include "lista.h"

#define TAM 10

struct lista {
    int tam;
    void **vet;
    int ini,fin,corr;
};

Lista *lst_cria(void) {
    Lista *l = (Lista*)malloc(sizeof(Lista));
    if (l==NULL) {
        printf("Erro na alocacao de memoria.\n");
        exit(1);
    }
    l->vet = (void**)malloc(TAM*sizeof(void*));
    if (l->vet==NULL) {
        printf("Erro na alocacao de memoria.\n");
        exit(1);
    }
    l->tam = 0;
    l-> ini = 0;
    l-> fin = 0;
    l-> corr = -1;
    return l;
}

int lst_vazia(Lista *l) {
    return (l->tam == 0);
}

void lst_insIni(Lista *l, void *x) {
    int i;
    if ((l->tam)==TAM) {
        printf("Há falta de espaço para insercao de novos elementos na lista.\n");
        return;
    }
    if (l->ini == -1) //atingiu a "outra ponta" da lista
        l->ini = TAM-1;
    i = l->ini;
    l->vet[i] = x;
    l->tam++;
    if (l->tam == 1) //elemento unico no array
        l->fin++;
    l->ini--;
}

void lst_insFin(Lista *l, void *x) {
    int i;
    if ((l->tam)==TAM) {
        printf("Há falta de espaço para insercao de novos elementos na lista.\n");
        return;
    }
    if (l->fin==TAM) //atingiu a "outra ponta" da lista
        l->fin = 0;
    i = l->fin;
    l->vet[i] = x;
    l->tam++;
    if (l->tam == 1) //elemento unico no array
        l->ini--;
    l->fin++;
}

void *lst_retIni(Lista *l) {
	int i = (l->ini)+1;
	if (lst_vazia(l)) 
	    return NULL;
	if (l->tam != 1) {
		if (l->corr == (l->ini)+1)
            l->corr = -1;
		l->ini++;
	}
	else { //Lista vai ficar vazia
		l->ini = 0;
		l->fin = 0;
		l->corr = -1;
	}
	l->tam--;
	return l->vet[i];
}

void *lst_retFin(Lista *l) {
	int i = (l->fin)-1;
	if (lst_vazia(l)) 
	    return NULL;
	if (l->tam != 1) {
		if (l->corr == (l->fin)-1)
            l->corr = -1;
		l->fin--;
	}
	else { //Lista vai ficar vazia
		l->ini = 0;
		l->fin = 0;
		l->corr = -1;
	}
	l->tam--;
	return l->vet[i];
}

void lst_posIni(Lista *l) { 
	if (lst_vazia(l))
	    l->corr = -1;
	else 
        l->corr = (l->ini)+1;
}

void lst_posFin(Lista *l) {
    if (lst_vazia(l))
        l->corr = -1;
    else
        l->corr = (l->fin)-1;
}

void *lst_prox(Lista *l) {
    int corr = l->corr;
    if (corr == -1 || l->corr == l->fin)
        return NULL;
    if (corr == TAM -1)
        l->corr = 0;
    else
        l->corr++;
    return l->vet[corr];
}

void *lst_ant(Lista *l) {
    int corr = l->corr;
    if (corr == -1 || l->corr == l->ini)
        return NULL;
    if (corr == 0)
        l->corr = TAM-1;
    else
        l->corr--;
    return l->vet[corr];
}

void lst_libera(Lista *l) {
    int i;
    void *aux;
    lst_posIni(l);
    aux = lst_prox(l);
	while (aux) {
	    i = l->corr;
		free(l->vet[i]);
		aux = lst_prox(l);
	}
	free(l->vet);
	free(l);
}