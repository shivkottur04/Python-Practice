class Queue:
    def __init__(self,max_size):
        self.queue=[]
        self.max_size=max_size
    def is_empty(self):
        return len(self.queue)==0
    def is_full(self):
        return len(self.queue)==self.max_size
    def enqueue(self,item):
        if self.is_full():
            print("Queue is full! Cannot enqueue item.")
        else:
            self.queue.append(item)
            print(f"Enqueued item: {item}")
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue item.")
            return None
        return self.queue.pop(0)
    def front(self):
        if self.is_empty():
            print("Queue is empty! No front item.")
        else:
            print("current front item:", self.queue[0])
    def display(self):
        if self.is_empty():
            print("Queue is empty! No items to display.")
        else:
            print("Queue items:", self.queue)       

if __name__ == "__main__":
    q=Queue(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)   

    q.enqueue(60)  # This will show that the queue is full

    q.display()

    front_lines=q.front()  # Display the front item

    if front_lines is not None:
        print("Front item:", front_lines)

    dequeued_item=q.dequeue()  # Dequeue an item
    if dequeued_item is not None:       
        print("Dequeued item:", dequeued_item)


    q.display()

    q.dequeue() 
    q.dequeue()
    q.dequeue()
    q.dequeue()  # This will show that the queue is empty            
