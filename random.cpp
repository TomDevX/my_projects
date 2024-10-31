#include <iostream>
#include <random>

int main() {
    // Create a random number engine
    std::random_device rd;  // Obtain a seed from the hardware
    std::mt19937 gen(rd()); // Seed the Mersenne Twister engine

    // Define distributions
    std::uniform_int_distribution<> int_dis(1, 100);   // Range from 1 to 100
    std::uniform_real_distribution<> real_dis(0.0, 1.0); // Range from 0.0 to 1.0

    // Generate and output random numbers
    int random_int = int_dis(gen);
    double random_real = real_dis(gen);

    std::cout << "Random integer: " << random_int << std::endl;
    std::cout << "Random real number: " << random_real << std::endl;

    return 0;
}