#include <iostream>
using namespace std;
void main(){
	const int N = 4;
	int mat[N*N];
	for (int i = 0; i < N*N; i++){
		mat[i] = i+1;
	}
	int up = 0; 
	int left = 0;
	int down = N-1;
	int right = N-1;
	int dir = 0;
	int row = 0;
	int col = 0;
	int num = 0;
	while (up < down | left < right){
		switch (dir){
		case 0:
			for (int i = 0; i < N; i++){
				if (col + i < right){
					num += 1;
					cout << mat[row*N + col + i] << " ";
				}
				else{
					up += 1;
					col += i;
					dir = 1;
					break;
				}
			}
		case 1:
			for (int i = 0; i < N; i++){
				if (row + i < down){
					num += 1;
					cout << mat[row*N + col + i*N] << " ";
				}
				else{
					right -= 1;
					row += i;
					dir = 2;
					break;
				}
			}
		case 2:
			for (int i = 0; i < N; i++){
				if (col - i > left){
					num += 1;
					cout << mat[row*N + col - i] << " ";
				}
				else{
					down -= 1;
					col -= i;
					dir = 3;
					break;
				}
			}
		case 3:
			for (int i = 0; i < N; i++){
				if (row - i > up){
					num += 1;
					cout << mat[row*N + col - i*N] << " ";
				}
				else{
					left += 1;
					row -= i;
					dir = 0;
					break;
				}
			}
		}
		if (num == N*N - 1){
			cout << mat[row * N + col] << endl;
		}
	}
}
