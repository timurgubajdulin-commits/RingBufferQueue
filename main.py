from script import RingBufferQueue


def main():
    queue = RingBufferQueue(3)

    print("is_empty:", queue.is_empty())
    print("is_full:", queue.is_full())
    print("size:", queue.size())
    print("peek:", queue.peek())
    print("dequeue:", queue.dequeue())
    print("to_list:", queue.to_list())

    queue.enqueue(1)
    print("enqueue(1):", queue.to_list())

    queue.enqueue(2)
    print("enqueue(2):", queue.to_list())

    queue.enqueue(3)
    print("enqueue(3):", queue.to_list())

    print("peek:", queue.peek())
    print("is_full:", queue.is_full())
    print("size:", queue.size())

    print("dequeue:", queue.dequeue())
    print("after dequeue:", queue.to_list())

    queue.enqueue(4)
    print("enqueue(4):", queue.to_list())

    queue.enqueue(5)

    print("dequeue:", queue.dequeue())
    print("dequeue:", queue.dequeue())
    print("dequeue:", queue.dequeue())
    print("dequeue:", queue.dequeue())

    print("is_empty:", queue.is_empty())


if __name__ == "__main__":
    main()