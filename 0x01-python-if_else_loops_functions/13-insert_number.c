#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into
 * a sorted singly linked list
 * @head: the head pointer
 * @number: the number to be inserted
 * Return: the address of the new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->n = NULL;
	while (current->next && current->next->n < number)
		current = current->next;
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
