String a = "hello";
String b = "!";

System.out.println(a+b);
System.out.println(a.append(b));

StringBuilder strBuilder = new StringBuilder(10);
strBuilder.append(a).append().append(b);
System.out.println(strBuilder.toString);