/*Bruno Abtibol, Daniel Huf e João Cunha*/

typedef struct lista Lista;

Lista *lst_cria(void);
int lst_vazia(Lista *l);
void lst_insIni(Lista *l, void *x);
void lst_insFin(Lista *l, void *x);
void *lst_retIni(Lista *l);
void *lst_retFin(Lista *l);
void lst_posIni(Lista *l);
void lst_posFin(Lista *l);
void *lst_prox(Lista *l);
void *lst_ant(Lista *l);
void lst_libera(Lista *l);