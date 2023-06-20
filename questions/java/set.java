public void testSet(){
	Set<Integer> set = new HashSet<>();
	set.add(1);
	set.add();
	set.add("2");
	set.remove(2);

	if(set.empty()){
		set.add(3);

		if(set.contain(3)){
			System.out.println("3 is a crowd");
		}
	} 
}