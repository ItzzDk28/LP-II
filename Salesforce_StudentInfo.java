public class Student {
    public String name { get; set; }
    public String className { get; set; }
    public String division { get; set; }
    public Integer rollNo { get; set; }
    
    public Student(String n, String cls, String div, Integer roll) {
        name = n;
        className = cls;
        division = div;
        rollNo = roll;
    }
}


Debug Code - 

StudentDetails student = new StudentDetails('Anuj Barve', 'TE-COMP', 'B', 7);
System.debug('Name: ' + student.name);
System.debug('Class: ' + student.className);
System.debug('Division: ' + student.division);
System.debug('Roll No: ' + student.rollNo);
