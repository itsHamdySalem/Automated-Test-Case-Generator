#include "../include/packet_validator.h"
#include <iostream>
#include <fstream>

PacketValidator::PacketValidator(int totalModules, const std::vector<int> &modules)
    : totalModules(totalModules), modules(modules)
{
    if (totalModules <= 0)
    {
        throw std::invalid_argument("Total number of modules must be greater than 0.");
    }
    for (int module : modules)
    {
        if (module < 1 || module > totalModules)
        {
            throw std::invalid_argument("Packet module numbers must be between 1 and the total number of modules.");
        }
    }
}

bool PacketValidator::isValidSequence(int currentModule, int nextModule)
{
    if (currentModule == totalModules)
    {
        return (nextModule == totalModules || nextModule == 1);
    }
    return (nextModule == currentModule || nextModule == currentModule + 1);
}

void PacketValidator::generateCSV(const std::string &filename)
{
    std::ofstream csvFile(filename);
    if (!csvFile.is_open())
    {
        std::cerr << "Error opening file!" << std::endl;
        return;
    }

    csvFile << "PacketID,ModuleNumber,ValidModule\n";
    for (size_t i = 0; i < modules.size(); ++i)
    {
        bool isValid = (i == 0) ? true : isValidSequence(modules[i - 1], modules[i]);
        csvFile << i + 1 << "," << modules[i] << "," << (isValid ? "Yes" : "No") << "\n";
    }

    csvFile.close();
    std::cout << "CSV file generated successfully!" << std::endl;
}
