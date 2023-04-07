import java.utils.*; //intentional

public class TestQueue {

	public void testQueue(){
		Queue<String> queue = new PriorityQueue<>();

		Deque<Integer> deque = new ArrayDeque<>();

		queue.add("1");
		deque.add(1);
		
		queue.add(2);
		deque.add("2")

		println(queue.peek());
		System.out.println(deque.peek())	
	}
}