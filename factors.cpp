#include "factors.h"
#include <iostream>
#include <fstream>
#include <cmath>

std::vector<std::pair<int, int>> factorize(int num) {
    std::vector<std::pair<int, int>> factors;
    for (int a = 2; a <= sqrt(num); ++a) {
        if (num % a == 0) {
	    factors.emplace_back(a, num / a);
        }
    }
    return factors;
}


void factorize_file(const std::string& file_path) {
    std::ifstream file(file_path);
    if (!file) {
        std::cerr << "Failed to open the file: " << file_path << std::endl;
        return;
    }

    int numb;
    while (file >> numb) {
        std::vector<std::pair<int, int>> factors = factorize(numb);
        for (const auto& factor : factors)
        {
            std::cout << numb << " = " << factor.first << " * " << factor.second << std::endl;
        }
    }
}
