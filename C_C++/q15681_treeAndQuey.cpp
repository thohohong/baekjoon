#include <iostream>
#include <vector>

using namespace std;

int N, R, Q;
vector<int> tree[100001];
bool check[100001] = {false, };
int dp[100001];

int dfs(int v){
  int sum = 1;
  
  if (dp[v] != 0) return dp[v];
  check[v] = true;

  for (int i : tree[v]){
    if (!check[i]){
      sum += dfs(i);
    }
  }
  dp[v] = sum;
  return sum;
}

int main(int argc, const char * argv[]) {
  
  cin.tie(0) -> sync_with_stdio(0);
  cin >> N >> R >> Q;
  
  int U, V;
  for (int i = 0; i < N-1; i++){
    cin >> U >> V;
    tree[U].push_back(V);
    tree[V].push_back(U);
  }

  dfs(R);
  int query;
  
  for (int i = 0; i < Q; i++){  
    cin >> query;
    printf("%d\n", dp[query]);
  }
}