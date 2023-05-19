#pragma once
#include <string>

class Character
{
	
};

class Health_Component
{
private:
	int16_t health;
	int16_t max_health;
	int16_t shield;
	int16_t max_shield;
public: 

	Health_Component(int16_t max_health, int16_t  max_shield)
		: health(max_health), shield(max_shield){}

	int16_t getHealth(){ return health; }
	int16_t getMax_health() { return max_health; }
	int16_t getShield() { return shield; }
	int16_t getMax_shield(){ return max_shield; }

	void setHealth(int16_t incH) {
		if (health + incH > max_health) {
			health = max_health;
		}
			health += incH;
	};

	void setShield(int16_t incS) { shield += incS; }

};