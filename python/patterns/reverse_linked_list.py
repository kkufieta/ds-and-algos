def reverse_linked_list(linked_list):
    prev = None
    current = linked_list.head

    while current:
        next = current.next
        current.next = prev

        prev = current
        current = next

    linked_list.head = prev

