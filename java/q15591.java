import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class q15591 {
    public static int bfs(ArrayList<int[]>[] edge, int k, int v){
        int result = 0;
        Queue<Integer> q = new LinkedList<>();
        boolean[] visit = new boolean[edge.length];

        for (int i = 0; i < edge.length; i++){
            visit[i] = false;
        }

        q.add(v);
        visit[v] = true;
        while (!q.isEmpty()){
            int cur = q.poll();
            for(int[] i : edge[cur]){
                if (i[1] >= k && !visit[i[0]]){
                    q.add(i[0]);
                    visit[i[0]] = true;
                    result++;
                }
            }
//            System.out.println("fuck");
        }
        return result;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int q = sc.nextInt();

        ArrayList<int[]>[] edge = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++){
            edge[i] = new ArrayList<>();
        }
        for (int i = 0; i < n-1; i++){
            int start = sc.nextInt();
            int end = sc.nextInt();
            int usado = sc.nextInt();

            int tmp_array1[] = {end, usado};
            int tmp_array2[] = {start, usado};

            edge[start].add(tmp_array1);
            edge[end].add(tmp_array2);
        }
        for (int i = 0; i < q; i++){
            int k = sc.nextInt();
            int v = sc.nextInt();
            int result = bfs(edge, k, v);
            System.out.println(result);
        }
    }
}
