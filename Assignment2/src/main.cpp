#include "../include/packet_validator.h"
#include <iostream>
#include <vector>
#include <limits>

int main()
{
    int numPackets;
    int totalModules;
    std::vector<int> modules;

    // Input totalModules with validation
    while (true)
    {
        std::cout << "Enter the total number of modules: ";
        std::cin >> totalModules;
        if (std::cin.fail() || totalModules <= 0)
        {
            std::cin.clear();                                                   // clear input buffer
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // discard invalid input
            std::cerr << "Invalid input. Please enter a positive integer for total number of modules." << std::endl;
        }
        else
        {
            break;
        }
    }

    // Input numPackets with validation
    while (true)
    {
        std::cout << "Enter the number of packets: ";
        std::cin >> numPackets;
        if (std::cin.fail() || numPackets <= 0)
        {
            std::cin.clear();                                                   // clear input buffer
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // discard invalid input
            std::cerr << "Invalid input. Please enter a positive integer for the number of packets." << std::endl;
        }
        else
        {
            break;
        }
    }

    // Input module numbers with validation
    std::cout << "Enter the module number for each packet:\n";
    for (int i = 0; i < numPackets; ++i)
    {
        int moduleNumber;
        while (true)
        {
            std::cin >> moduleNumber;
            if (std::cin.fail() || moduleNumber < 1 || moduleNumber > totalModules)
            {
                std::cin.clear();                                                   // clear input buffer
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // discard invalid input
                std::cerr << "Invalid input. Please enter a module number between 1 and " << totalModules << "." << std::endl;
            }
            else
            {
                modules.push_back(moduleNumber);
                break;
            }
        }
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
