# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -Wall -std=c++17 -Iinclude

# Target executable
TARGET = packet_validator.exe

# Source files
SOURCE_FILES = src/main.cpp src/packet_validator.cpp

# Object files
OBJECTS = $(SOURCE_FILES:.cpp=.o)

# Default rule
all: $(TARGET)

# Link object files to create executable
$(TARGET): $(OBJECTS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJECTS)

# Compile source files into object files
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean up object files and executable
clean:
	$(RM) $(OBJECTS) $(TARGET)

# Phony targets
.PHONY: all clean
