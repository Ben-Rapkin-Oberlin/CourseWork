#include <string>
#include <vector>
#include <cctype>
#include <array>

using namespace std;

//not used to simply statistics
extern vector<string> knownNames;

//not used to simply statistics
int varNames(string line);

int tabSpace(string line);

int equalSpacing(string line);

int emptyLine(string line);

vector<int> verboseif(string line);

vector<int> increment (string line);

int dotSpace(string line);

int imports(string line);

float mainsize(string fname);

array<float, 10> train(string a);