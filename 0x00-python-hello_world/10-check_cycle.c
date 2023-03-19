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
	listint_t *cycle, *ncycle;

	cycle = ncycle = list;

	while (cycle && ncycle && ncycle->next)
	{
		/* cycle will move one node while nloop moves 2 */
		cycle = cycle->next;
		ncycle = ncycle->next->next;

		if (cycle == ncycle)
		{
			/* there is a cycle here */
			return 1;
		}
	}
	return 0;
}
