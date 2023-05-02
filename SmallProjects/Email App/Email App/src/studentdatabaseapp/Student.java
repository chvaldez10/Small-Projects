package studentdatabaseapp;

import java.util.Scanner;

public class Student {
    private String firstName;
    private String lastName;
    private int gradeYear;
    private String studentID;
    private String courses="";
    private int tuitionBalance = 0;
    private static int costOfCourse = 600;
    private static int id = 100;

    public Student(){
        Scanner in = new Scanner(System.in);
        System.out.print("enter student first name: ");
        this.firstName = in.nextLine();

        System.out.print("enter student last name: ");
        this.lastName = in.nextLine();

        System.out.print("1 - for freshman\n2 - for sophmore\n3 - for junior\n4 - for senior\nenter student grade level: ");
        this.gradeYear = in.nextInt();

        setStudentID();
    }

    private void setStudentID(){
        id++;
        this.studentID = gradeYear + "" + id;
    }

    public void enroll() {
        boolean keepEntering = true;

        do {
            System.out.print("Enter course to enroll (Q to quite): ");
            Scanner in = new Scanner(System.in);
            String course = in.nextLine().toUpperCase();

            if (course.equals("Q")) {
                keepEntering = false;
            } else{
                courses = courses + "\n" + course;
                tuitionBalance += costOfCourse;
            }
        } while (keepEntering);
    }

    public void viewBalance() {
        System.out.println("Your balance is: $" + tuitionBalance);
    }

    public void payTuition(){
        viewBalance();
        System.out.print("Enter your payment: $");
        Scanner in = new Scanner(System.in);
        int payment = in.nextInt();

        tuitionBalance -= payment;
        System.out.println("Thank you for your payment of: $" + payment);
        viewBalance();
    }

    public String showInfo(){
        return "Name: " + firstName + " " + lastName +
                "\nCourses Enrolled:" + courses +
                "\nBalance: $" + tuitionBalance;
    }
}
