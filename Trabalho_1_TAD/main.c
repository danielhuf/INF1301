#include <stdio.h>
#include <stdlib.h>
#include "lista.h"

/*NOTAS: 1. Troquei o valor dos exit para 1. Lembro do Ivan utilizando 1 nos exemplos dele.
         2. Em lst_insIni e lst_insFin, inicializei a variável aux no inicio da função, em vez de criá-la
         somente no else.
         3. Dei uma alterada nas funções lst_posIni e lst_posFin, acho que ficou mais simples.
         De qualquer maneira o código original ta no evernote. 
         4. Fiz uma pequena alteração em lst_prox e lst_ant, tive que criar um aux porque
         senao poderia haver o caso de l->corr ser igual a nulo, e quando retornasse l->corr->ant 
         não daria cero, porque retornaria o ant de um NULL. De qualquer maneira o código original ta no 
         evernote. */
         
void exibeLista(Lista *f) {
    int *aux;
    puts("=== Elementos da Lista ***");
    lst_posIni(f);
    aux=(int*)lst_prox(f);
    while(aux) {
        printf("%d\n",*aux);
        aux=(int*)lst_prox(f);
        }
    }

int main(void) {
    Lista *f=lst_cria();
    int *a=(int*) malloc(sizeof(int));
    int *b=(int*) malloc(sizeof(int));
    int *c=(int*) malloc(sizeof(int));
    int *d=(int*) malloc(sizeof(int));
    int *aux;
    *a=10;
    *b=20;
    *c=30;
    *d=40;
    
    lst_insFin(f,a);
    lst_insFin(f,b);
    lst_insFin(f,c);
    lst_insFin(f,d);
    
    exibeLista(f);                                
    aux=lst_retIni(f);
    printf("*** Elemento Retirado %d ***\n",*aux);   
    
    exibeLista(f);
    aux=lst_retIni(f);
    printf("*** Elemento Retirado %d ***\n",*aux);
    
    exibeLista(f);
    aux=lst_retFin(f);
    printf("*** Elemento Retirado %d ***\n",*aux); 
    
    exibeLista(f);                                 
    aux=lst_retFin(f);                      
    printf("*** Elemento Retirado %d ***\n",*aux);
    
    exibeLista(f);
    exibeLista(f);
    lst_libera(f);

    return 0;
}
