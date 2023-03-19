#include "lists.h"
/**
 * check_cycle - funv=ction that checks if a singly linked
 * list has a cycle
 *
 * @list: pointer to the singly linked list
 * Return: 0 if no cycle and 1 if there is
 */
int check_cycle(listint_t *list);
{
	listint_s *loop, *nloop;

	loop = nloop = head;

	while (loop && nloop && nloop->)
	{
		/* loop will move one node while nloop moves 2*/
		loop = loop->next;
		nloop = nloop->next->next;
		if (loop == nloop)
		{
			/* there is a cycle here*/
			return 1
		}
	}
	return 0
}
