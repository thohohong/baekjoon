
#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

// fail at 50%...
// I guess its problem was in overflow/underflow. 

int* data, * tree;

int treeInit(int start, int end, int node) {
	if (start == end) return tree[node] = data[start];
	int mid = (start + end) / 2;
	return tree[node] = treeInit(start, mid, node * 2) * treeInit(mid + 1, end, node * 2 + 1);
}


int update(int start, int end, int idx, int modify, int node) {
	if (idx < start || idx > end) return tree[node];

	if (start == end) return tree[node] = modify;
	int mid = (start + end) / 2;	
	return tree[node] = update(start, mid, idx, modify, node * 2) * update(mid + 1, end, idx, modify, node * 2 + 1);
}


int multiply(int range_L, int range_R, int start, int end, int node) {
	if (range_R < start || range_L > end) {
		//현재 범위가 구하려는 범위 밖일 때
		return 1;
	}
	else if (range_L <= start && range_R >= end) {
		//현재 범위가 구하려는 범위 안일 때
		return tree[node];
	}
	else {
		int mid = (start + end) / 2;
		int result = multiply(range_L, range_R, start, mid, node * 2) * multiply(range_L, range_R, mid + 1, end, node * 2 + 1);
		return result;
	}
}

int main() {
	int N, K;
	int result;

	while (scanf("%d %d", &N, &K) != EOF) {

		data = (int*)malloc(sizeof(int) * N);
		tree = (int*)malloc(sizeof(int) * N * 10);

		for (int i = 0; i < N; i++) {
			scanf("%d", &data[i]);
		}
		scanf("%*c");

		treeInit(0, N - 1, 1);

		for (int i = 0; i < K; i++) {
			char cmd;
			int num1, num2;

			scanf("%c %d %d", &cmd, &num1, &num2);
			scanf("%*c");

			switch (cmd) {
			case 'C':
				update(0, N - 1, num1 - 1, num2, 1);
				break;
			case 'P':
				result = multiply(num1 - 1, num2 - 1, 0, N - 1, 1);
				if (result < 0) printf("-");
				else if (result == 0) printf("0");
				else printf("+");
				break;
			}
		}
		printf("\n");
	}
	return 0;
}