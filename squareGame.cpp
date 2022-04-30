//DONALD GLOVER LOVERS
//Joe Fernandez, Zachary Moore, and William Jenkins
#include<iostream>
#include<vector>
#include <string>
using namespace std;
void swap(char &num1, char &num2){
	char num3;
	num3=num1;
	num1=num2;
	num2=num3;
}
void printGrid(char stuff[5][5]){
for(int i =0; i<5; i++){
          cout << stuff[i][0];
          for(int j=1; j<5; j++){
                  cout << " " << stuff[i][j];
          }
          cout << endl;
  }
}
int main(int argc, char** argv){
  vector<string> lines;
  string s;
  getline(cin, s);
  char grid[5][5];
  int bX, bY;
  while( !cin.eof() ){
    lines.push_back(s);
    getline(cin, s);
  }
  int i = 0;
  for( string line : lines ){
    cout << "Line " << ++i << " is " << line << endl;
  }
  for(int i = 0; i < 5; i++){
  	for(int j=0; j<5; j++){
		grid[i][j]=lines[i][j];
		if(lines[i][j]==' '){
			bX=j;
			bY=i;
		}
	}
  }
  printGrid(grid);
  cout << endl;
  string steps=lines[5];
  for(int i=0; i<steps.length(); i++){
  	switch(steps[i]){
		case 'L':
			if(bX-1<0){
				cout << "Out of bounds" << endl;
				return 0;
			}
			swap(grid[bY][bX], grid[bY][bX-1]);
			bX--;
			break;
		case 'B':
			if(bY+1>4){
				cout << "Out of bounds" << endl;
				return 0;
			}
			swap(grid[bY][bX], grid[bY+1][bX]);
			bY++;
			break;
		case 'A':
			if(bY-1<0){
				cout << "Out of bounds" << endl;
				return 0;
			}
			swap(grid[bY][bX], grid[bY-1][bX]);
			bY--;
			break;
		case 'R':
			if(bX+1>4){
				cout << "Out of bounds" << endl;
				return 0;
			}
			swap(grid[bY][bX], grid[bY][bX+1]);
			bX++;
			break;
		default:
			cout << "INPUT ERROR" << endl;
			return 0;
	}
	printGrid(grid);
	cout << endl<< endl;
  }
  printGrid(grid);
  return 0;
}
