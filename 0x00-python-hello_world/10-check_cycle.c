#include "lists.h"

/**
 * check_cycle - fuction that validates if cycle exist on a
 * single linked list.
 * @list: head of linked list
 * Return: 1 if cycle exists or 0 if not.
 */

int check_cycle(listint_t *list)
{
	listint_t *p = list, *p1 = list;

	if (!list)
		return (0);
	p = p->next;
	p1 = p1->next->next;

	while (p && p1 && p1->next)
	{
		if (p == p1)
			return (1);
		p = p->next;
		p1 = p1->next->next;
	}
	return (0);
}
