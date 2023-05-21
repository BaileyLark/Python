#include <iostream>
#include <string>
#include "Classes.h"

void printer() { std::cout << "working"; }

int main() {

	Stats_Component statsTesting = Stats_Component(4, 5, 3);
	std::cout << statsTesting.getStats()[0] << "\n"; 
}




// unanmed namescape, contents can only be accessed inside file
// inline namespace, the default (if multiple of the same name exist)

// function pointer
//void (*ptr)() = &printer; // has to be in brackets otherwise it calls the function void* ptr()
//(*ptr)(); // dereference then pass the value through
