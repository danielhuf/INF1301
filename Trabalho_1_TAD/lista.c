/*Bruno Abtibol, Daniel Huf e João Cunha*/

#include <stdlib.h>
#include <stdio.h>
#include "lista.h"

typedef struct no {
    void *info;
    struct no *prox;
    struct no *ant;
} No;

struct lista {
    int tam;
    No *ini;
    No *fin;
    No *corr;
};

Lista *lst_cria(void) {
    Lista *l = (Lista*)malloc(sizeof(Lista));
    if (l == NULL) {
		printf("Memoria insuficiente.\n");
		exit(1);
	}
    l->tam = 0;
    l->ini = NULL;
    l->fin = NULL;
    l->corr = NULL;
    return l;
}

int lst_vazia(Lista *l) {
    return (l->tam == 0);
}

void lst_insIni(Lista *l, void *x){
    No *aux, *novo = (No*)malloc(sizeof(No));
    if (novo == NULL) {
		printf("Memoria insuficiente.\n");
		exit(1);
	}
    novo->info = x;
    if (l->ini == NULL) {  //lista vazia
        l->ini = novo;
        l->fin = novo;
        novo->prox = NULL;
    }
    else {
        aux = l->ini;
        novo->prox = aux;
        aux->ant = novo;
        l->ini = novo;
    }
    novo->ant = NULL;   //ele é o "primeiro da fila"
    l->tam++;
}

void lst_insFin(Lista *l, void *x){
    No *aux, *novo = (No*)malloc(sizeof(No));
    if (novo == NULL) {
        printf("Memoria insuficiente.\n");
		exit(1);
	}
    novo->info = x;
    if (l->fin == NULL){ //lista vazia
        l->ini = novo;
        l->fin = novo;
        novo->ant = NULL;
    }
    else {
        aux = l->fin;
        novo->ant = aux;
        aux->prox = novo;
        l->fin = novo;
    }
    novo->prox = NULL; //ele é o "último da fila"
    l->tam++;
}

void *lst_retIni(Lista *l) {
    void *info;
    No *aux = l->ini;
    if (lst_vazia(l))
        return NULL;
    if (l->tam != 1) {  //elemento nao é o unico da lista
        l->ini = aux->prox;
        l->ini->ant = NULL;
    }
    else 
        l->ini = NULL;   //zera a lista
    l->tam--;
    info = aux->info;
    if (l->corr == aux)
        l->corr = NULL;
    free(aux);
    return info;
}

void *lst_retFin(Lista *l) {
    void *info;
    No *aux = l->fin;
    if (lst_vazia(l))
        return NULL;
    if (l->tam!=1) {    //elemento nao é o unico na lista
        l->fin = aux->ant;
        l->fin->prox = NULL;
    }
    else 
        l->fin = NULL;      //zera a lista
    l->tam--;
    info = aux->info;
    if (l->corr == aux)
        l->corr = NULL;
    free(aux);
    return info;
}

void lst_posIni(Lista *l) { 
	if (lst_vazia(l))
	    l->corr = NULL;
	else 
        l->corr = l->ini;
}

void lst_posFin(Lista *l) {
    if (lst_vazia(l))
        l->corr = NULL;
    else
        l->corr = l->fin;
}

void *lst_prox(Lista *l) {
    No *aux;
    if (l->corr == NULL)
        return NULL;
    aux = l->corr;
    l->corr = l->corr->prox;    
    return aux->info;
}

void *lst_ant(Lista *l) {
    No *aux;
    if (l->corr == NULL)
        return NULL;
    aux = l->corr;
    l->corr = l->corr->ant;
    return aux->info;
}

void lst_libera(Lista *l) {
    lst_posIni(l);
    No *aux = l->corr;
    while (l->corr != NULL) {
        l->corr = aux->prox; //Quando l->corr for NULL, significa que aux é o último elemento
        free(aux->info);
        free(aux);
        aux = l->corr;
    }
    free(l);
}