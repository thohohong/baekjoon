import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class q1600_monkey_wtb_horse {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int min = Integer.MAX_VALUE;
        Queue<int[]> q = new LinkedList<>();
        int[] dx = { -1, -2, -2, -1,  1,  2,  2,  1, -1,  0, 1, 0 };
        int[] dy = { -2, -1,  1,  2,  2,  1, -1, -2,  0, -1, 0, 1 };
        int[] dx_m = {-1,  0,  1,  0 };
        int[] dy_m = { 0, -1,  0,  1 };

        int k = sc.nextInt();
        int w = sc.nextInt();
        int h = sc.nextInt();

        int[][] board = new int[h][w];
        int[][] visit = new int[h][w];

        for (int i = 0; i < h; i++){
            for (int j = 0; j < w; j++){
                board[i][j] = sc.nextInt();
                visit[i][j] = k + 1;
            }
        }

        int[] status = {0, 0, 0, 0};
        q.add(status);

        while (!q.isEmpty()){
            status = q.poll();
            int x = status[0];
            int y = status[1];

            if (x == w - 1 && y == h - 1){
                System.out.println(status[3]);
                return;
            }

            if (x >= 0 && x < w && y >= 0 && y < h && visit[y][x] > status[2] && board[y][x] == 0){
                visit[y][x] = status[2];
            }
            else {
                continue;
            }

            // add components
            if (status[2] >= k){
                for (int i = 0; i < 4; i++){
                    int[] new_status = new int[4];
                    new_status[0] = x + dx_m[i];
                    new_status[1] = y + dy_m[i];
                    new_status[2] = status[2];
                    new_status[3] = status[3] + 1;
                    q.add(new_status);
                }
            }
            else {
                for (int i = 0; i < 12; i++){
                    int[] new_status = new int[4];
                    new_status[0] = x + dx[i];
                    new_status[1] = y + dy[i];
                    if (i < 8){
                        new_status[2] = status[2] + 1;
                    }
                    else {
                        new_status[2] = status[2];
                    }
                    new_status[3] = status[3] + 1;
                    q.add(new_status);
                }
            }
        }

        System.out.println(-1);


    }
}
