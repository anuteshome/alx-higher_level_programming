#include "lists.h"

/**
 * check_cycle - checks if a listint_t list has a cycle in it
 * @list: the head of list
 *
 * Return: 0 if there is no cycle, 1 if there is a cylce
 */
int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	if (list == NULL)
		return (0);
	fast = list->next;
	slow = list;
	while (fast != NULL && slow != NULL && fast->next != NULL)
	{
		if (fast == slow)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}

	return (0);
}
