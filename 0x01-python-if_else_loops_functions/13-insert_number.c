#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *aux;
	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	aux = *head;

	while (aux->next)
	{
		if (number <= aux->n)
		{
			new->next = aux;
			*head = new;
			return (new);
		}
		if (number >= aux->n && number <= aux->next->n)
		{
			new->next = aux->next;
			aux->next = new;
			return (new);
		}
		if (!aux->next->next)
		{
			aux->next->next = new;
			return (new);
		}
		aux = aux->next;
	}
	return (new);
}
