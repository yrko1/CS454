#include <iostream>
#include <stdlib.h>
#include <unistd.h>
#include <string>
#include <cstring>
using namespace std;

int main(int argc, const char * argv[]){
	string a=argv[1];
	string b=argv[2];
	string c=a+" "+b;
	int status = system(c.c_str());
	return 0;
}

