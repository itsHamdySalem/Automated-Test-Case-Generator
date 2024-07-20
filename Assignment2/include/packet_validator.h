#ifndef PACKET_VALIDATOR_H
#define PACKET_VALIDATOR_H

#include <vector>
#include <string>

/**
 * @class PacketValidator
 * @brief Class to validate and generate CSV report for packet sequences based on module rules.
 */
class PacketValidator
{
private:
    int totalModules;
    std::vector<int> modules;

    /**
     * @brief Validates if the sequence of the next packet is correct based on the current packet's module.
     * @param currentModule Module number of the current packet.
     * @param nextModule Module number of the next packet.
     * @return True if the next packet is valid, otherwise false.
     */
    bool isValidSequence(int currentModule, int nextModule);

public:
    /**
     * @brief Constructor for PacketValidator.
     * @param totalModules Total number of modules.
     * @param modules Vector containing the module number for each packet.
     */
    PacketValidator(int totalModules, const std::vector<int> &modules);

    /**
     * @brief Generates a CSV file with validation results.
     * @param filename Name of the CSV file to be generated.
     */
    void generateCSV(const std::string &filename);
};

#endif // PACKET_VALIDATOR_H
