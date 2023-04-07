Map<String, Integer> strToNum = new HashMap<>(){"one":1,"two":"2","three":"3, four":4};

for(Map.Entry<String,Integer> entry: strToNum.entrySet()){
	System.out.println("key:"+ entry.key()+ " value:"+ entry.value());
}