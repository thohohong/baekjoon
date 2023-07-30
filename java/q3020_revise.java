import java.util.Arrays;
import java.util.Scanner;

public class q3020_revise {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int width = sc.nextInt();
        int height = sc.nextInt();
        int[] cave_up = new int[height + 1];
        int[] cave_down = new int[height + 1];

        for (int i = 0; i < height; i++){
            cave_up[i] = 0;
            cave_down[i] = 0;
        }

        for (int i = 0; i < width; i++){
            int get = sc.nextInt();
            if (i % 2 == 0){
                cave_down[get]++;
            }
            else {
                cave_up[get]++;
            }
        }
        int sum = 0;
        int min = width;
        int min_num = 1;

        int[] prefix_sum_up = new int[height + 1];
        int[] prefix_sum_down = new int[height + 1];
        prefix_sum_down[height] = 0;
        prefix_sum_up[height] = 0;

        for (int i = height - 1; i >= 0; i--){
            prefix_sum_down[i] = prefix_sum_down[i + 1] + cave_down[i];
            prefix_sum_up[i] = prefix_sum_up[i + 1] + cave_up[i];
        }

        for (int i = 0; i < height; i++){
            sum = 0;
            sum += prefix_sum_up[i + 1];
            sum += prefix_sum_down[height - i];

            if (sum < min) {
                min = sum;
                min_num = 1;
            }
            else if (sum == min) {
                min_num++;
            }
        }

        System.out.println(min + " " + min_num);
    }
}
