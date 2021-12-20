#include "lists.h"
/**
 * check_cycle - check cycle 
 * @cycle: cycle
 * Return: 0 or 1
 */

int check_cycle(listint_t *cycle)
{
	listint_t *cycle_1 = cycle;
	listint_t *cycle_2 = cycle;

	if (!cycle)
		return (0);

	while (cycle_1 && cycle_2 && cycle_2->next)
	{
		cycle_1 = cycle_1->next;
		cycle_2 = cycle_2->next->next;
		if (cycle_1 == cycle_2)
			return (1);
	}

	return (0);
}
