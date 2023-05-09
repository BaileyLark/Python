#include <iostream>
#include <string>

class Planet
{


}



int main()
{

	int hello{ 15 };
	int* hello2{ &hello };

	std::cout << hello << hello2 << std::endl;

};