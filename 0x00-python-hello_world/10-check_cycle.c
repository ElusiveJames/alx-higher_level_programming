#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr = NULL;
	listint_t *speed = NULL;
	listint_t *head = list;

	if (list == NULL)
		return (0);
	ptr = head;
	speed = head;
	while (ptr->next != NULL)
	{
		if (ptr->next == head)
			return (1);
		ptr = ptr->next;
		speed = speed->next->next;
		if (speed == NULL)
			return (0);
		if (speed == ptr)
			return (1);
	}

	return (0);
}
