#include <string>
#include <vector>
#include <cctype>
#include <array>

#include <iostream>
#include <fstream>

#include "readers.h"

using namespace std;

// extern int vector<string> knownNames;

array<float, 10> train(string a)
{   
    //std::cout<<a<<"\n";
    array<float, 10> info = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    // string fname = "C:\\Users\\benra\\Documents\\Academics\\Spring 22\\Systems (241)\\finalProject\\smallp.c"
    fstream newfile;
    newfile.open(a, ios::in);

    // TODO make imports abs count
    // TODO make comment/multy comment tester

    // imports
    int icount = 0; // wholefreq
    // file lines
    int linec = 0;
    //'=' vs ' = '
    int eSpace = 0;
    int ecount = 0; // ratiofreq
    // mainsize
    float r = mainsize(a); // wholefreq
    // tab vs spaces
    int tspace = 0;
    int tcount = 0; // ratiofreq
    // empty lines
    int mspace = 0; // wholefreq
    // !NULL
    int verbose = 0; // ratiofreq
    int nVerbose = 0;
    // .'\n'
    int newLine = 0; // ratiofreq
    int dots = 0;
    // increment
    int total = 0;
    int sinc, sdec, cinc, cdec, vinc, vdec; // simple, complex, verbose
    sinc = sdec = cinc = cdec = vinc = vdec = 0;
    bool val = false;

    vector<int> names(11, 0); // 10 indexes initialized to 0
    //std::cout << '\n';
    if (newfile.is_open())
    { // checking whether the file is open
        string line;

        while (getline(newfile, line))
        {
            linec++;
            // std::cout << line << "   "  << linec << " c\n";

            /////
            // std::cout << "workin1";
            icount += imports(line);

            ///
            // std::cout << "workin2";
            int a = equalSpacing(line);
            if (a)
            {
                eSpace += a;
                ecount++;
            }

            ////
           // std::cout << "workin3";
            a = tabSpace(line);
            if (a)
            {
                tspace += a;
                tcount++;
                // std::cout << "val: "<< tspace<< " tcount: "<< tcount <<'\n';
            }

            ////
            // std::cout << "workin4";
            a = emptyLine(line);
            if (a)
            {
                mspace++;
            }

            ////
            //::cout << "workin5";
            try{
                vector<int> b = verboseif(line);
            //std::cout << line << " trip aaaa \n";

                if (b[0] != 0)
                {
                    nVerbose += b[0];
                }
                if (b[1] != 0)
                {
                    verbose += b[1];
                }
            }
            catch (const std::exception &e)
            {
                std::cout <<"\n\n\n trip aaaa \n";
                std::cerr << e.what() << '\n';
                std::cout << line << "   " << linec << " c\n";
                
            }

            ////
           // std::cout <<" trip 6 3\n";
            try
            {

                a = varNames(line);
                if (a != 0)
                {
                    names[a] = names[a] + 1;
                }
            }
            catch (const std::exception &e)
            {
                std::cerr << e.what() << '\n';
                std::cout << line << "   " << linec << " c\n";
                std::cout << line << " trip 6 ";
            }

            ////
            // std::cout << "workin7*";
            a = dotSpace(line);
            if (a == 1)
            {
                newLine++;
            }
            if (a > 1)
            {
                dots += (a - 1);
                // std::cout << "seq:" << line << "   " << linec << " " << (a - 1) << " c\n";
            }

            //
           //  std::cout << "workin8";
            vector<int> b = increment(line);
            for (auto i : b)
            {
                if (i > 0)
                {
                    val = true;
                    break;
                }
            }
            if (val)
            {
                sinc += b[0];
                sdec += b[1];
                cinc += b[2];
                cdec += b[3];
                vinc += b[4];
                vdec += b[5];

                total = total + b[0] + b[1] + b[2] + b[3] + b[4] + b[5];
            }

            val = false;
            //std::cout << "workin9";
        }
    }
    /*
    std::cout << "workin1";
    std::cout << "imports: " << icount << '\n';
    std::cout << "Main Ratio: " << r << '\n';

    std::cout << "espace: " << (float)eSpace / ecount << '\n';
    std::cout << "tspace: " << (float)tspace / tcount << '\n';
    std::cout << "nspace: " << (float)mspace / linec << '\n';
    std::cout << "Verbose: " << (float)verbose / nVerbose << '\n';
    std::cout << "dotSpace: " << (float)dots / newLine << '\n';

    std::cout << '\n';

    std::cout << "++: " << (float)sinc / total << '\n';
    std::cout << "--: " << (float)sdec / total << '\n';
    std::cout << "+=: " << (float)cinc / total << '\n';
    std::cout << "-=: " << (float)cdec / total << '\n';
    std::cout << "a=a+1: " << (float)vinc / total << '\n';
    std::cout << "a=a-1: " << (float)vdec / total << '\n';




    for (auto i : names)
    {
        std::cout << i << ", ";
    }

    std::cout << '\n';
    for (auto i : knownNames)
    {
        std::cout << i << ", ";
    }
    */
   //prevents any /0 errors
    info[0] = (icount!=0) ? (float)icount : 0;
    info[1] = (ecount!=0) ? (float)(eSpace / ecount) : 0;
    info[2] = (tcount!=0) ? (float)(tspace / tcount) : 0;
    info[3] = (linec!=0) ? (float)(mspace / linec) : 0;
    info[4] = (nVerbose!=0) ? (float)(verbose / nVerbose) : 0;
    info[5] = (newLine!=0) ? (float)(dots / newLine) : 0;
    info[6] = (total!=0) ? (float)((sinc + sdec) / total) : 0;
    info[7] = (total!=0) ? (float)((cinc + cdec) / total) : 0;
    info[8] = (total!=0) ? (float)((vinc + vdec) / total) : 0;
    info[9] = (r!=0) ? r : 0;

    return info;

    // call each method
    // add those to runing total
    // repeat
    // save to file/profile
}