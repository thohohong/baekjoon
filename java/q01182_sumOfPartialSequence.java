import java.util.Scanner;
import java.util.Vector;

public class q01182_sumOfPartialSequence {
    public static int S;
    public static int N;
    public static Vector<Integer> sequence;
    
    static int DFS(int i, int sum) {
        if (i == N) {
            if (sum == S) {
                return 1;
            }
            else {
                return 0;
            }
        }
        int result = 0;

        // not include i
        result += DFS(i+1, sum);

        // include i
        result += DFS(i+1, sum + sequence.get(i));

        return result;
    }

    public static void main(String argv[]) {
        Scanner sc = new Scanner(System.in);
        sequence = new Vector<Integer>();

        N = sc.nextInt();
        S = sc.nextInt();

        for (int i = 0; i < N; i++){
            sequence.add(sc.nextInt());
        }

        int result = DFS(0, 0);
        if (S == 0) result--;
        System.out.print(result);
    }
}