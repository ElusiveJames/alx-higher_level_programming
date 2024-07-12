#include <stdio.h>
#include "lists.h"

int check_cycle(listint_t *list)
{   
    listint_t *ptr = NULL;
    listint_t *head = list;

    if (list == NULL)
        return (0);
    ptr = head;
    while (ptr->next != NULL)
    {
        if (ptr->next == head)
            return (1);
        ptr = ptr->next;
    }

    return (0);
    
}