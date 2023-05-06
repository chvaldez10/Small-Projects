package emaillapp;
import java.util.Scanner;

public class EmailApp {
    public static void main(String[] args) {
        System.out.print("Enter first name: ");
        Scanner input = new Scanner(System.in);
        String firstName = input.nextLine();

        System.out.print("Enter lst name: ");
        String lastName = input.nextLine();

        System.out.print("Enter company: ");
        String company = input.nextLine();
        
        Email em1 = new Email(firstName, lastName, company);
        String info = em1.showInfo();
        System.out.println(info);
    }
}