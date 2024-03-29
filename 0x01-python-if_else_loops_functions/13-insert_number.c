/**
  *insert_node - add node at a position
  *@head: pointer to head of list
  *@number: integer value to be inserted
  *Return: pointr to new node
  */
#include <stddef.h>
#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
listint_t *insert_node(listint_t **head, int number)
{
	struct listint_s *ptr;
	struct listint_s *new_n;

	if(head == NULL)
		return NULL;


	new_n =  malloc(sizeof(struct listint_s));

	if (new_n == NULL)
	{
		free(new_n);
		return (NULL);
	}
	ptr = *head;
	new_n->n = number;

	if (*head == NULL)
	{
		new_n->next = NULL;
		*head = new_n;
		return (new_n);
	}
	if (ptr->n > number)
	{
		new_n->next = ptr;
		*head = new_n;
		return (new_n);
	}
	while (ptr->next != NULL)
	{
		if (ptr->next->n > new_n->n)
		{
			new_n->next = ptr->next;
			ptr->next = new_n;
			return new_n;
		}
		ptr = ptr->next;
	}
	ptr->next = new_n;
	new_n->next = NULL;
	return (new_n);
}
