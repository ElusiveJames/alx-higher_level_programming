#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
* is_palindrome - check if linkend list is palinddrome
* @head: pointer to start of list
* Return: 1 if palindrome 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	listint_t *temp = NULL;
	int *elements = NULL;
	int len, j, i;

	if (head == NULL)
		return (1);
	temp = *head;
	i = 0;

/* get length of list */
	while (temp != NULL)
	{
		temp = temp->next;
		i++;
	}
/* allocate memory */
	elements = malloc(sizeof(int) * i);
	if (elements == NULL)
		return (0);
	temp = *head;
	i = 0;
	/* store list in array */
	while (temp != NULL)
	{
		elements[i] = temp->n;
		temp = temp->next;
		i++;
	}
	len = i - 1;
	j = 0;
	/* check if palindrome */
	while (j <= len)
	{
		if (elements[j] != elements[len])
			return (0);
		j++;
		len--;
	}
	free(elements);
	return (1);
}
