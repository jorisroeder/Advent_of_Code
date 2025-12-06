import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class tag_1 {
  static int current_number = 50;
  static int counter = 0;
  static int x;

  public static void main(String[] args) throws FileNotFoundException {

    Scanner scanner = new Scanner(new File("input.txt"));
    while (scanner.hasNextLine()) {
      String i = scanner.nextLine();

      char direction = i.charAt(0);
      int number = Integer.parseInt(i.substring(1));
      // System.out.println("Output!");
      // System.out.println(direction + " " + number);
      switch (direction) {
        case 'R' -> {
          x = 1;
        }
        case 'L' -> {
          x = -1;
        }
        default -> System.out.println("Fehler");
      }

      for (int j = 0; j < number; j++) {
        current_number += x;

        current_number = ((current_number % 100) + 100) % 100;
        if (current_number == 0) {
          counter++;
        }

      }
    }

    System.out.println(counter);
    scanner.close();
  }

}