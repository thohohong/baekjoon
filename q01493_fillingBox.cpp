#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <math.h>

using namespace std;
int N;
//vector<pair<int, int>> cube;
//vector<int> cube;
int cube[21];

void sort3int(int *a, int *b, int *c) {
  if (*a < *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
  }
  if (*a < *c) {
    int tmp = *a;
    *a = *c;
    *c = tmp;
  }
  if (*b < *c) {
    int tmp = *b;
    *b = *c;
    *c = tmp;
  }
}

int devide(int l, int w, int h) {
  int result = 0;
  int min = l;

  
  if (l == 0 || w == 0 || h == 0){
    return 0;
  }
  if (w < min) min = w;
  if (h < min) min = h;

  int square = (int)(log(min) / log(2));
  int len = -1;

  for (int i = square; i >= 0; i--){
    if (cube[i] > 0) {
      result = 1;
      cube[i]--;
      len = pow(2, i);
      break;
    }
  }

  if (len == -1) {
    return -1;
  }
  
  int result1 = devide(l, w, h-len);
  int result2 = devide(l-len, w, len);
  int result3 = devide(len, w-len, len);

  if (result1 == -1 || result2 == -1 || result3 == -1) {
    return -1;
  }
  else {
    return 1 + result1 + result2 + result3;
  }
}

int main(void) {
  // Get Input
  int l, w, h;
  
  // vector<pair<int, int>> cube;

  cin >> l;
  cin >> w;
  cin >> h;

  cin >> N;

  int A, B;
  for (int i = 0; i < N; i++){
    cin >> A;
    cin >> B;
    cube[A] = B;
  }


  int result = devide(l, w, h);
  cout << result;  
}