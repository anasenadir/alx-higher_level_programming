#include "lists.h"

/**
 * get_len - get the length of a linked list
 * @head: the head pointer
 * Return: the length of the list
 */
int get_len(listint_t *head)
{
	listint_t *current = head;
	int len = 0;

	while (current)
	{
		len += 1;
		current = current->next;
	}
	return (len);
}


/**
 * is_palindrome - function that checks if a
 * singly linked list is a palindrome
 * @head: the head pointer
 * Return: 0 if it is not a palindrome
 *          1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	int *arr_ptr, list_len, i, j;
	listint_t *current = *head;

	list_len = get_len(*head);
	if (list_len == 0)
		return (1);

	arr_ptr = malloc(list_len + 1);
	
	if (!arr_ptr)
		return (1);
	
	for (i = 0; i < list_len; i++)
	{
		arr_ptr[i] = current->n;
		current = current->next;
	}

	i = 0;
	j = list_len - 1;

	while (i < j)
	{
		if (arr_ptr[i] != arr_ptr[j])
			return (0);
		i += 1;
		j -= 1;
	}

	free(arr_ptr);
	return (1);
}
