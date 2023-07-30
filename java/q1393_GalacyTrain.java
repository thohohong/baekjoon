import java.util.Scanner;

public class q1393_GalacyTrain {
    // It's Like yeot S1BAL
    public static int gcd(int a, int b){
        if (b == 0){
            return a;
        }
        else {
            return gcd(b, a%b);
        }
    }
    public static double getDistance(int from_x, int from_y, int to_x, int to_y){
        return Math.sqrt(Math.pow(from_x - to_x, 2) + Math.pow(from_y - to_y, 2));
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean unreachable = false;

        int sx = sc.nextInt();
        int sy = sc.nextInt();

        int ex = sc.nextInt();
        int ey = sc.nextInt();

        int origin_dx = sc.nextInt();
        int origin_dy = sc.nextInt();
        int dx = origin_dx;
        int dy = origin_dy;

        int x = 0;
        int y = 0;

        //in case of Vertical line
        if (dx == 0 && dy == 0){
            unreachable = true;
        }
        else if (dy == 0){
            x = sx;
            y = ey;
            if ((x - ex) / origin_dx < 0){
                unreachable = true;
            }
        }
        // in case of Parallel line
        else if (dx == 0){
            x = ex;
            y = sy;
            if ((y - ey) / origin_dy < 0){
                unreachable = true;
            }
        }
        else {
            int gcd_ = gcd(dx, dy);
            dx /= gcd_;
            dy /= gcd_;

            double pre_dis = 400;
            double cur_dis = 400;
            x = ex;
            y = ey;
            cur_dis = getDistance(sx, sy, x, y);

            while(pre_dis > cur_dis){
                pre_dis = cur_dis;
                x += dx;
                y += dy;

                cur_dis = getDistance(sx, sy, x, y);
            }

            x -= dx;
            y -= dy;

            if ((x - ex) / origin_dx < 0){
                unreachable = true;
            }
        }

        if (unreachable){
            x = ex;
            y = ey;
        }

        System.out.println(x + " " + y);
    }
}
