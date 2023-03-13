#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - function that checks if list is a palindrome
 * @head: Start of the list
 *
 * Return: 0 if not palindrome else 1
 */
int is_palindrome(listint_t **head)
{
	int i, count = 0;
	listint_t *node, **array;if (!head || !*head)
		return (1);
	
	/* count the number of nodes in the list */
	for (node = *head; node; node = node->next)
		count++;
	
	/* allocate memory for an array of pointers to nodes */
	array = malloc(sizeof(listint_t *) * (count / 2));
	if (!array)
		return (0);

	/* store the first half of the list in the array */
	for (i = 0, node = *head; i < count / 2; i++, node = node->next)
		array[i] = node;
	
	/* compare the second half of the list with the first half in reverse */
	for (i = count % 2 ? count / 2 + 1 : count / 2; i < count; i++, node = node->next)
		if (node->n != array[count - i - 1]->n)
			break;
	
	/* free the memory allocated for the array */
	free(array);
	
	/* return 1 if the list is a palindrome, 0 otherwise */
	return (i == count);
}
