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
    if not linked_list.head or not linked_list.head.next:
        return

    end_of_1st_half, p_slow, p_fast = None, linked_list.head, linked_list.head
    while p_fast != None and p_fast.next != None:
        end_of_1st_half = p_slow
        p_slow = p_slow.next
        p_fast = p_fast.next.next

    previous, current = None, p_slow
    while current:
        next_ = current.next
        current.next = previous
        previous = current
        current = next_

    end_of_1st_half.next = previous