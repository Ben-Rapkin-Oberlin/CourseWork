#include <string>
#include <vector>
#include <cctype>

#include <iostream>
#include <fstream>

using namespace std;

// Globle/language specific, this would be for decideing between authors

// imports

// finds number of imports
// tested and working
int imports(string line)
{
    // assume only one include per line
    if (line.find("include") != string::npos)
    {
        return 1;
    }
    return 0;
}

// finds relative size of main in file
// tested and working
float mainsize(string fname)
{
    fstream newfile;
    newfile.open(fname, ios::in);
    int bracket = 0;
    int mlinecount = 0;
    int alinecount = 0;
    int start = 0;

    if (newfile.is_open())
    { // checking whether the file is open
        string line;
        while (getline(newfile, line))
        {
            alinecount++;
            if (start != 0)
            {
                mlinecount++;
            }
            if (line.find(" main(") != string::npos)
            {
                start++;
                // std::cout << "true\n";
            }

            vector<size_t> positions;
            if (start && line.find("}") != string::npos)
            {

                size_t index = line.find("}", 0);
                while (index != string::npos)
                {
                    positions.push_back(index);
                    index = line.find("}", index + 1);
                }
                bracket -= positions.size();
            }

            if (start && line.find("{") != string::npos)
            {
                size_t index = line.find("{", 0);
                while (index != string::npos)
                {
                    positions.push_back(index);
                    index = line.find("{", index + 1);
                }
                bracket += positions.size();
                // std::cout << "adding: " << positions.size() << "\n";
            }

            if (start != 0 && bracket == 0)
            {
                start--;
            }
            // std::cout << bracket;
        }
    }
    return (float)mlinecount / alinecount;
}

// file number

// functions/main length
// exacution speed
