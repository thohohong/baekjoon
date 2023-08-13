import java.util.*;
import java.io.*;

public class Main {
	static int N;
	static long X;
	static long[][] dp;
	
	static long dfs(int n, long x) {
		if (n == 0) return 1;
		long result = 0;
		
		if (x == 1) return 0;
		else if (x < dp[n-1][0] + 2) {
			result += dfs(n-1, x - 1);
		} else if (x == dp[n-1][0] + 2) {
			result += dp[n-1][1] + 1;
		} else if (x > dp[n-1][0] + 2) {
			result += dp[n-1][1] + 1 + dfs(n-1, x-(dp[n-1][0]+2));
		}		
		return result;
		// An = 1 + An-1 + 1 + An-1 + 1;
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		X = Long.parseLong(st.nextToken());
		dp = new long[N+1][2];
		
		dp[0][0] = 1;
		dp[0][1] = 1;
		
		
		for (int i = 1; i <= N; i++) {
			dp[i][0] = dp[i-1][0] * 2 + 3;
			dp[i][1] = dp[i-1][1] * 2 + 1;
		}
		
		long result = dfs(N, X);
		
		System.out.println(result);
	}
}
