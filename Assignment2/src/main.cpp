#include "../include/packet_validator.h"
#include <iostream>
#include <vector>

int main()
{
    int numPackets;
    int totalModules;
    std::vector<int> modules;

    std::cout << "Enter the total number of modules: ";
    std::cin >> totalModules;

    std::cout << "Enter the number of packets: ";
    std::cin >> numPackets;

    std::cout << "Enter the module number for each packet:\n";
    for (int i = 0; i < numPackets; ++i)
    {
        int moduleNumber;
        std::cin >> moduleNumber;
        modules.push_back(moduleNumber);
    }

    try
    {
        PacketValidator validator(totalModules, modules);
        validator.generateCSV("./output/packet_validation.csv");
    }
    catch (const std::invalid_argument &e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
