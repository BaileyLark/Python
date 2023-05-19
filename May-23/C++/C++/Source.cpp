#include <iostream>
#include <string>
#include "Classes.h"

int main() {
	Health_Component testing = Health_Component(5, 5);
	std::cout << testing.getHealth() << std::endl;
	testing.setHealth(2);
	std::cout << testing.getHealth() << std::endl;
}

// 