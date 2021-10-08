import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Info {
    int row;
    int col;
    boolean broke;
    int move;

    Info(int row_, int col_, boolean broke_, int move_) {
        row = row_;
        col = col_;
        broke = broke_;
        move = move_;
    }

    void setBroke(boolean broke_){
        broke = broke_;
    }

    void move(){
        move++;
    }
}

public class q2206_break_wall {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int row = sc.nextInt();
        int col = sc.nextInt();
        int[][] map = new int[row][col];
        int[][] visit = new int[row][col];

        int result = -1;

        int[] dx = { 0,  1,  0, -1 };
        int[] dy = { 1,  0, -1,  0 };

        for (int i = 0; i < row; i++){
            String line = sc.next();
            for (int j = 0; j < col; j++){
                map[i][j] = line.charAt(j) - '0';
            }
        }

        Queue<Info> q = new LinkedList<>();

        q.add(new Info(0, 0, false, 1));

        while(!q.isEmpty()){
            Info cur = q.poll();

            if (cur.row == row - 1 && cur.col == col - 1){
               result = cur.move;
               break;
            }
            if (cur.row >= row || cur.row < 0 || cur.col >= col || cur.col < 0){
                continue;
            }

            if (map[cur.row][cur.col] == 1){
                if (cur.broke){
                    continue;
                }
                else {
                    cur.setBroke(true);
                }
            }
            if (visit[cur.row][cur.col] == 0){
                if (cur.broke){
                    visit[cur.row][cur.col] = 2;
                }
                else {
                    visit[cur.row][cur.col] = 1;
                }
            }
            else if (visit[cur.row][cur.col] == 1) {
                continue;
            }
            else if (visit[cur.row][cur.col] == 2 && !cur.broke){
                visit[cur.row][cur.col] = 1;
            }
            else {
                continue;
            }

            for (int i = 0; i < 4; i++){
                q.add(new Info(cur.row + dx[i], cur.col + dy[i], cur.broke, cur.move + 1));
            }
        }

        System.out.println(result);
    }
}
