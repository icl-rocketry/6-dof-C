#include <iostream>
#include <string>
#include <fstream>
#include <Eigen/Dense>


double getValue_2D(double x, double y, const std::string& filename) {

    std::ifstream aero_csv(filename);
    if (!aero_csv.is_open()) {
        std::cerr << "Could not open file" << filename << std::endl;
        return 0;
    }

    std::string line;
    std::vector<>

    while(std::getline(aero_csv, line)) {
        

    }
}