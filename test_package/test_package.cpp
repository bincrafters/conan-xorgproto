#include <iostream>
#include <X11/X.h>

int main()
{
    std::cout << "X11 protocol version: " << X_PROTOCOL << "." << X_PROTOCOL_REVISION << std::endl;
    return 0;
}
