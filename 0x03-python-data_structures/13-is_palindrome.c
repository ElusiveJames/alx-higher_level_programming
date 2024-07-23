#include "lists.h"
#include <stddef.h>
/**
* is_palindrome - check if linkend list is palinddrome
* @head: pointer to start of list
* Return: 1 if palindrome 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	listint_t *temp = NULL;
	int data[100];
	int len, j;

	if (head == NULL)
		return (1);
	temp = *head;
	int i = 0;

	while (temp != NULL)
	{
		data[i] = temp->n;
		temp = temp->next;
		i++;
	}
	len = i - 1;
	j = 0;
	while (j <= len)
	{
		if (data[j] != data[len])
			return (0);
		j++;
		len--;
	}
	return (1);
}
