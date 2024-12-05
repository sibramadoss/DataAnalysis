using System;

class HelloWorld {
    static void MyMethod(string fname) {
    Console.WriteLine(fname + " Refsnes");
    }

    static void Main()
    {
        for (int i = 0; i<3; i++){
            Console.WriteLine(i);
            MyMethod(Console.ReadLine());
        }
    }
}

