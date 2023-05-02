package emaillapp;

import java.lang.reflect.Constructor;
import java.util.Scanner;

public class Email {
    private String firstName;
    private String lastName;
    private String email;
    private String password;
    private int defaultPasswordLength = 10;
    private String department;
    private int mailboxCapacity = 500;
    private String alternateEmail;
    private String companySuffix = "anycompany.com";

    //    Constructor to receive the first name and last name
    public Email(String firstName, String lastName, String company){
        this.firstName = firstName;
        this.lastName = lastName;
        this.companySuffix = company;
        this.department = setDepartment();

        this.password = randomPassword(defaultPasswordLength);
        System.out.println("\nYou password: " + this.password);

        email = firstName.toLowerCase() + "." + lastName.toLowerCase()+ "@" + department + "." + companySuffix;
    }

    //    Ask for the department
    private String setDepartment() {
        System.out.print("\n1 for sales\n2 for development\n3 for accounting\n0 for none\nEnter department code: ");
        Scanner in = new Scanner(System.in);
        int departmentChoice = in.nextInt();

        if (departmentChoice == 1) {return "sales";}
        else if (departmentChoice == 2) {return "development";}
        else if (departmentChoice == 3) {return "accounting";}
        else {return "";}
    }

    private String randomPassword(int length) {
        String passwordSet = "abcdefghijklmnopzrstuvwxyz012346789!@#$%^&*";
        char[] password = new char[length];
        for (int i=0; i<length; i++) {
            int rand = (int) (Math.random() * passwordSet.length());
            password[i] = passwordSet.charAt(rand);
        }

        return new String (password);

    }

    public void setMailboxCapacity(int capacity){
        this.mailboxCapacity = capacity;
    }

    public void setAlternateEmail(String altEmail){
        this.alternateEmail = altEmail;
    }

    public void changePassword(String password){
        this.password = password;
    }

    public int getMailboxCapacity() {return mailboxCapacity; }
    public String getAlternateEmail() {return alternateEmail; }
    public String getPassword() { return password; }

    public String showInfo() {
        return "\nUser: " + firstName + " " + lastName + "; " + "Company Email: " +
                email + "; "+ "Mailbox Capacity" + mailboxCapacity + " MB";
    }

}
