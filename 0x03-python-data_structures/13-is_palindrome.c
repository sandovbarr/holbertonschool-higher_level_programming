#include "lists.h"

/**
 * is_palindrome - function in C that checks if a
 * singly linked list is a palindrome.
 * @head: pointer to head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *aux = *head, *aux2 = aux;
	int iter = 0, iter2 = 0, iter3 = 0;

	if (aux && !aux->next)
		return (1);

	while (aux->next)
	{
		aux = aux->next;
		iter2++;
	}
	aux2 = aux;
	aux = *head;
	iter3 = iter2 / 2;

	while (aux->n == aux2->n)
	{
		aux = aux->next;
		aux2 = *head;
		while (aux2 && iter < iter2 - 1)
		{
			aux2 = aux2->next;
			iter++;
		}
		if ((iter2 == iter3 + 2 && aux->n == aux2->n) ||
			(iter2 < iter3 || iter2 == 0))
		{
			return (1);
		}
		iter = 0, iter2--;
	}
	return (0);
}
