import java.util.*;
import java.io.*;

// 스택이 비어있을 수 있음에 주의할 것
// static으로 선언한 멤버 변수를 main에서 잘 사용하고 있는지 확인할것
public class Main {
	static int L, C;
	static char[] chars, result;
	static boolean[] isVowel;
	static StringBuilder sb = new StringBuilder();
	
	static void comb(int cnt, int start, int conCnt, int vowCnt) {
		if (cnt == L) {
			if (vowCnt < 1 || conCnt < 2) return;
			for (char c : result) sb.append(c);
			sb.append("\n");
			return;
		}
		
		for (int i = start; i < C; i++) {
			result[cnt] = chars[i];
			if (isVowel[i]) comb(cnt+1, i+1, conCnt, vowCnt+1);
			else comb(cnt+1, i+1, conCnt+1, vowCnt);
		}
		
		
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		L = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		
		chars = new char[C];
		result = new char[L];
		isVowel = new boolean[C];
		
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < C; i++) {
			chars[i] = st.nextToken().charAt(0);
		}
		
		Arrays.sort(chars);
		for (int i = 0; i < C; i++) {
			if (chars[i] == 'a' || chars[i] == 'e' || chars[i] == 'i' || chars[i] == 'o' || chars[i] == 'u') {
				isVowel[i] = true;
			}
		}
		comb(0, 0, 0, 0);
		
		System.out.print(sb.toString());
		br.close();
	}
}
