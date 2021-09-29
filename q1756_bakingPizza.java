import java.util.Scanner;

public class q1756_bakingPizza {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int depth = sc.nextInt();
        int num = sc.nextInt();

        int[] oven = new int[depth];
        int[] pizza = new int[num];

        for (int i = 0; i < depth; i++){
            oven[i] = sc.nextInt();
        }

        for (int i = 0; i < num; i++){
            pizza[i] = sc.nextInt();
        }

        int min_size = oven[0];

        for (int i = 0; i < depth; i++){
            if (oven[i] > min_size){
                oven[i] = min_size;
            }
            else {
                min_size = oven[i];
            }
        }

        int pizza_idx = 0;
        int depth_idx = depth - 1;

        while(depth_idx >= 0 && pizza_idx != num){
            if (oven[depth_idx] >= pizza[pizza_idx]){
                pizza_idx++;
            }
            depth_idx--;
        }

        if (num != pizza_idx){
            System.out.println(0);
        }
        else {
            System.out.println(depth_idx + 2);
        }

    }
}
