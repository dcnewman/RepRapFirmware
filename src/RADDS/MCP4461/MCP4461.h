#ifndef MCP4461_H
#define MCP4461_H

#include <inttypes.h>

class MCP4461 {

public:
	MCP4461() {};
	void begin() const {};
	void setMCP4461Address(uint8_t) const {};
	void setVolatileWiper(uint8_t, uint16_t) const {};
	void setNonVolatileWiper(uint8_t, uint16_t) const {};
};

#endif //MCP4461_H
