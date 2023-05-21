#pragma once
#include <string>
#include <array>

class Character
{
private:
	std::string cname;
	int16_t ccarryweight;
	//Components
	Stats_Component cstats = Stats_Component(2, 3, 4);
	//Health_Component chealth = Health_Component(100, 100);
	//Weapon CWeapon = Weapon();
	//Shield CShield = Shield();
public: 
	Character() {
	};	
};

class Weapon
{
};

class Stats_Component
{
private:
	int16_t maxhealth;
	int16_t maxshield;
	int16_t agility;
public:
	Stats_Component(int16_t h, int16_t ms, int16_t ag)
		: maxhealth(h), maxshield(ms), agility(ag) {}
	Stats_Component()
		: maxhealth(1), maxshield(1), agility(1){}
	std::array<int16_t, 3> getStats() {
		std::array<int16_t, 3>ar{ maxhealth, maxshield, agility }; 
		return ar; 
	}
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
		: health(max_health), shield(max_shield), max_health(max_health), max_shield(max_shield){}
	int16_t getHealth(){ return health; }
	int16_t getMax_health() { return max_health; }
	int16_t getShield() { return shield; }
	int16_t getMax_shield(){ return max_shield; }

	void setHealth(int16_t incH) {
		if (health + incH > max_health || health - incH < 0) {
			health = max_health;
		}
		else 
			health += incH;
	};
	void setShield(int16_t incS) {
		if (health + incS > max_shield || health - incS < 0) {
			shield = max_shield;
		}
		else
			shield += incS;
	};
};