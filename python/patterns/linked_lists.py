# Reverse a singly linked list
def reverse_linked_list(linked_list):
    prev = None
    current = linked_list.head

    while current:
        next = current.next
        current.next = prev

        prev = current
        current = next

    linked_list.head = prev


# Reverse the 2nd half of a singly linked list
def reverse_2nd_half(linked_list):
    return 