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
	struct listint_s *new_n = malloc(sizeof(struct listint_s));

	ptr = *head;

	if (new_n == NULL)
	{
		free(new_n);
		return (NULL);
	}
	new_n->n = number;

	if (*head == NULL)
	{
		printf("List is empty");
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
	while (ptr != NULL)
	{
		if ((ptr->n < new_n->n) && (ptr->next->n > new_n->n))
		{
			new_n->next = ptr->next;
			ptr->next = new_n;
			return new_n;
		}
		ptr = ptr->next;
	}
	ptr = new_n;
	new_n->next = NULL;
	return (new_n);
}
