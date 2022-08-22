from requests import head

#given n

itr = head

count = 1
while itr.next:
    count += 1
    itr = itr.next

if count == 0:
    return head.next

# 1 --> 2 --> 3 --> 4 --> 5

itr = head

index = 1
while itr.next:
    if count - n == 0:
        return head.next
    if index == count - n:
        itr.next = itr.next.next
        return head
    itr = itr.next
    index += 1

return head





