package com.Javapoint;
import java.util.Scanner;
public class Miniproject {
    public static void main(String[] args) {
        // Mini project - Guess the number game
        Scanner sc = new Scanner(System.in);
        int myNumber = (int) (Math.random() * 100); // Generate random number (1-100)

        int userNumber=0; // Declare initialization outside the loop

        do {
            System.out.println("Guess my number (1-100):");
            userNumber = sc.nextInt();

            if (userNumber == myNumber) {
                System.out.println("WOOHOO...CORRECT NUMBER");
                break;
            } else if (userNumber > myNumber) {
                System.out.println("Your number is too large");
            } else {
                System.out.println("Your number is too small");
            }
        } while (userNumber != myNumber); // Check if user guessed correctly

        System.out.println("My number was:");
        System.out.println(myNumber);
    }
}
