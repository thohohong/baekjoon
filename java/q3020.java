import java.util.Scanner;

public class q3020 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int width = sc.nextInt();
        int height = sc.nextInt();
        int[] cave = new int[width];

        for (int i = 0; i < width; i++){
            cave[i] = sc.nextInt();
        }
        int min = width;
        int min_num = 1;

        for (int i = 0; i < height; i++){
            int sum = 0;
            for (int j = 0; j < width; j++){
                if (j % 2 == 0){ //even number, from bottom
                    if (height - i <= cave[i]) {
                        sum++;
                    }
                }
                else { // odd number
                    if (height - i >= cave[i]) {
                        sum++;
                    }
                }
            }
            if (sum < min){
                min = sum;
                min_num = 1;
            } else if (sum == min){
                min_num++;
            }
        }

        System.out.println(min + " " + min_num);
    }
}
