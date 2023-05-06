package studentdatabaseapp;

import java.util.Scanner;

public class StudentDatabaseApp {
    public static void main(String[] args) {
        System.out.print("Enter the number of students you want to enroll: ");
        Scanner in = new Scanner(System.in);
        int numOfStudents = in.nextInt();

        Student[] students = new Student[numOfStudents];

        for(int i=0; i<numOfStudents; i++){
            students[i] = new Student();
            students[i].enroll();
            students[i].payTuition();
            String studentInfo = students[i].showInfo();

            System.out.println(studentInfo);
        }
    }
}
