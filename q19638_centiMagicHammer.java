import java.util.*;

public class q19638_centiMagicHammer {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int height_centi = sc.nextInt();
        int hammer_num = sc.nextInt();

        PriorityQueue<Integer> heights = new PriorityQueue<>(Collections.reverseOrder());

        for (int i = 0; i < n; i++){
            int temp = sc.nextInt();
            heights.add(temp);
        }

        int i = 0;
        for (i = 0; i < hammer_num; i++){
            int temp = heights.poll();
            if (temp < height_centi){
                heights.add(temp);
                break;
            }
            if (temp == 1) {
                heights.add(1);
                break;
            }
            heights.add(temp / 2);
        }

        int max_h = heights.poll();
        if (max_h < height_centi){
            System.out.println("YES");
            System.out.println(i);
        }
        else {
            System.out.println("NO");
            System.out.println(max_h);
        }
    }
}
