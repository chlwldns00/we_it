class ClassA {
    ClassA() {
        System.out.print("A");
        this.prn();
    }
    void prn() {
        System.out.print("B");

    }
    void prn(int x) {
        System.out.print("x");
    }
}

class ClassB extends ClassA {
    ClassB() {
        super();
        System.out.print("D");
    }

    void prn() {
        System.out.print("E");
    }
    
    void prn(int x) {
        System.out.print(x);

    }
}
public class Test {
    public static void main(String[] args) {
        int x =7;
        ClassA cal=new ClassB();
        cal.prn(x);
    }
}
