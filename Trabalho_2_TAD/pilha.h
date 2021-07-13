/*Bruno Abtibol, Daniel Huf e João Pedro Cunha*/

typedef struct pilha Pilha;

Pilha *pilha_cria(void);
int pilha_vazia(Pilha *p);
void pilha_push(Pilha *p, void *v);
void *pilha_pop(Pilha *p);
void pilha_libera(Pilha *p);