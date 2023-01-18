#include <string>
#include <vector>
#include <cctype>

#include <iostream>
#include <fstream>

#include <algorithm>

using namespace std;

vector<string> knownNames;

// Tab vs Spaces
// tested and working
int tabSpace(string line)
{
    // assume it will be first char
    // 0 for error/niether, 1 for tab, 2 for space
    char tab = char(9);
    try
    {
        if (line.at(0) == tab)
        {
            return 1;
        }
        else if (line.at(0) == ' ')
        {
            return 2;
        }
        else
        {
            return 0;
        }
    }

    catch (const std::exception &e)
    {
        return 0;
    }
}

// TODO consider multiple declarations per line
// TODO consider array names
// Other than TODO, tested and working
int varNames(string line)
{ // right now plan to store in profile
    // strip start
    size_t offset = 0;
    size_t startI;
    size_t endI;

    int names = 0;

    bool dash = false;
    bool underScore = false;
    // vscode changes tab to space
    char tab = char(9);
    int a = tabSpace(line);

    // assumes tabs will only be used at the start of a line
    if (a == 1)
    { // there are tabs and we are removing them
        while (line.find(tab) != string::npos)
        {
            line = line.substr(line.find(tab) + 1);
        }
    }
    if (a == 2)
    {
        while (!isalpha(line.at(offset)))
        {
            offset++;
            if (offset >= line.length())
            {
                return 0;
            }
        }
    }

    // TODO
    // check for multiple varibles: int a,b =0;
    /*if (line.find(",")!=string::npos){
    }
    */

    size_t Eindex = line.find("=");
    if (Eindex != string::npos && line.find("==") == string::npos && line.find("===") == string::npos)
    {
        if (offset >= Eindex)
        {
            offset = 0;
        }
        string var = line.substr(offset, Eindex - offset);
        // at this point, var is of form int a_a, A_A, a-a, aa, AA, Aa
        // so now we trim it to "a_a" and add it to knownNames
        endI = var.length() - 1;

        while (!isalpha(var.at(endI)))
        {
            endI--;
        }
        startI = endI;
        bool a = true;
        // consider a-a or a_a
        while (a && startI != 0)
        {
            if (!isalpha(var.at(startI - 1)))
            {
                // we are at either index 4 in "int aa" or index 6 in "int a_a"
                if (var.at(startI - 1) == '-')
                {
                    startI--;
                    dash = true;
                }
                else if (var.at(startI - 1) == '_')
                {
                    startI--;
                    underScore = true;
                }

                else
                {
                    a = false;
                }
            }
            else
            {
                startI--;
            }
        }
        var = var.substr(startI, endI - startI + 1);

        // if var is already in knowNames it's naming convention has been recorded
        // Thus we return as we don't want to count "int a;" and "a=3;" as seperate
        // varibles
        if (std::find(knownNames.begin(), knownNames.end(), var) != knownNames.end())
        {
            return 0;
        }

        knownNames.push_back(var);
        if (underScore)
        {
            // snake_Case,
            size_t Uindex = var.find("_");
            if (isupper(var.at(Uindex + 1)))
            {
                // upper or snake
                if (isupper(var.at(Uindex - 1)))
                {
                    // upper A_A
                    names = 1;
                }
                else
                {
                    // snake a_A
                    names = 2;
                }
            }
            else
            {
                // lower a_a
                // assuming no odD_case
                names = 3;
            }
        }
        else if (dash)
        {
            //- means kabab-case
            size_t Dindex = var.find("-");
            if (isupper(var.at(Dindex + 1)))
            {
                // upper A-A or a-A
                if (isupper(var.at(Dindex - 1)))
                {
                    // upper A-A
                    names = 4;
                }
                else
                {
                    // snake a-A
                    names = 5;
                }
            }
            else
            {
                // lower a-a
                // assuming no odD_case
                names = 6;
            }
        }
        else
        {
            int capCount = 0;
            for (int i = 0; i < (int)var.size(); i++)
            {
                if (isupper(var.at(i)))
                {
                    capCount++;
                }
            }
            if (capCount == 1)
            {
                // camelCase
                names = 7;
            }
            else if (capCount == 2 && var.length() > 2)
            {
                // CapitalCase
                names = 8;
            }
            else if (capCount >= 2)
            {
                // all caps
                names = 9;
            }
            else
            {
                // flat or single word, undescriptive
                names = 10;
            }
        }
        // call profile to store prevelance
    }
    return names;
}

// ' = ' vs '='
// tested and working
int equalSpacing(string line)
{
    // return 1 for " = " and 2 for "=" and 0 for none
    // assume at most one assigment (=) per line and not = && == on same line
    size_t Eindex = line.find("=");
    if (Eindex != string::npos && line.find("==") == string::npos && line.find("===") == string::npos)
    {
        if (line.at(Eindex - 1) == ' ' && line.at(Eindex + 1) == ' ')
        {
            return 1;
        }
        else
        {
            return 2;
        }
    }
    return 0;
}

// Empty Lines
// tested and working
int emptyLine(string line)
{
    // allow ' ' '\n' tab
    for (int i = 33; i < 127; i++)
    {
        if (line.find(char(i)) != string::npos)
        {
            return 0;
        }
    }
    return 1;
}

// (a!=NULL) vs (a)
// (a==NULL) vs (!a)
// (a==0) vs (!a)
// (a!=0) vs (a)
// c doesn't have TRUE FALSE, TRUE= !0, False=0, Null is present
// does not consiter a statment like: result = a > b ? x : y;
// tested and working
vector<int> verboseif(string line)
{
    //std::cout<<"1\n";
    vector<int> count = {0, 0}; // [0] for applicable but not verbose, [1] for applicable and verbose
    if (line.find("if") != string::npos)
    {
        if (line.find("if") > line.find("/") && line.find("/") != string::npos) // check to make sure not reading a comment
        {                                                                       // i have both becuase I'm not sure how int compares to string::npos
            return count;
        }
        // c doesn't have 'or' 'and'
        vector<string> list;
    //std::cout<<"1\n";
        list.push_back(line);
        // split if statment into args, first &&
        // "if (a || b && c || d)" -> "if (a || b ", " c||d)"
        for (int i = 0; i < (int)list.size(); i++)
        { 
        //std::cout<<"1.1\n";
            string temp = list[i];
            //std::cout<<temp<<"\n"; 
            if (temp.find("&") != string::npos)
            {
                //std::cout<<"1.2\n";
                try{
                    list[i] = temp.substr(0, line.find("&"));
                    list.push_back(temp.substr(line.find("&") + 2));
                    i = 0;
                }
                catch (const std::exception &e) {
                    std::cout<< list[i]<<" *Error\n";
                }
             // std::cout<<"1.3\n";
            }
        
        }
   // std::cout<<"3\n";
        // now further split by ||
        //"if (a || b ", " c||d)" -> "if (a ", " b ", " c", " d)"
        for (int i = 0; i < (int)list.size(); i++)
        {
            string temp = list[i];
            if (temp.find("|") != string::npos)
            {
                list[i] = temp.substr(0, temp.find("|"));
                list.push_back(temp.substr(temp.find("|") + 2));
            }
        }
        // now check each arg
        for (auto i : list)
        {
            // not currently considering a==1, maybe be being used in a none boolean sense

            if (i.find("<") != string::npos || i.find(">") != string::npos)
            {
                continue; // just here to stop it from checking every other statment
            }
            // current possible args: (a!=NULL), (a), (a==NULL), (!a), (a==0), (a!=0)
            else if (i.find("NULL") != string::npos)
            {
                count[1] = count[1] + 1; // verbose
            }
            // current possible args: (a), (!a), (a==0), (a!=0)
            else if (i.find("==0") != string::npos || i.find("!=0") != string::npos)
            {
                count[1] = count[1] + 1; // verbose
            }
            // current possible args: (a), (!a) and we will assume it is one of these
            else if (i.find("==") == string::npos)
            {
                count[0] = count[0] + 1;
            }
            //std::cout<<"3\n";
        }
    }
    return count;
}
// run "C:\Users\benra\Documents\Academics\Spring 22\Systems (241)\finalProject\Data\Ben&Gawain\freq.c"
// ++ vs -- vs +=1 vs -=1
// TODO: a=a+1
// tested and working
vector<int> increment(string line)
{
    //++ -- += -= these corraspond to vector indexes
    // could combine into '--' + '++' vs '+=' + '-+' to show
    // stylistic inc dec instead. Will have to think on it
    vector<int> a = {0, 0, 0, 0, 0, 0};
    // a line can have multiple inc and dec
    string temp = line;
    while (temp.find("++") != string::npos)
    {
        a[0] = a[0] + 1;
        temp = temp.substr(temp.find("++") + 2);
    }
    temp = line;
    while (temp.find("--") != string::npos)
    {
        a[1] = a[1] + 1;
        temp = temp.substr(temp.find("--") + 2);
    }
    temp = line;
    while (temp.find("+=") != string::npos)
    {
        a[2] = a[2] + 1;
        temp = temp.substr(temp.find("+=") + 2);
    }
    temp = line;
    while (temp.find("-=") != string::npos)
    {
        a[3] = a[3] + 1;
        temp = temp.substr(temp.find("-=") + 2);
    }
    if (a[0] != 0 && a[1] != 0 && a[2] != 0 && a[3] != 0)
    {
        // assume no one is evil and typing a=a++;
        // this is probaly faster than a for loop right?
        string temp = line;
        temp.erase(std::remove_if(temp.begin(), temp.end(), ::isspace), temp.end());
        // from ' a = a+ 1 ' to 'a=a+1'
        // assume only one of these can happen per line
        for (auto i : knownNames)
        {
            if (temp.find(i + "=" + i + "1"))
            {
                a[4] = a[4] + 1;
                break;
            }
            else if (temp.find(i + "=" + i + "1"))
            {
                a[5] = a[5] + 1;
                break;
            }
        }
    }
    return a;
}

// \n after .
// tested and working
int dotSpace(string line)
{
    // 0 for no dot, 1 for dot && spaceing, 2+ for dot no spacing
    // this is becuase .foo.boo will count as two lines if spaced,
    // but only one if not
    char tab = char(9);
    if (line.find("#include") != string::npos)
    { // it will pick up header files like "stdio.h"
        return 0;
    }

    size_t dotIndex = line.find(".");
    if (dotIndex != string::npos)
    {
        if (line.find("//") != string::npos && line.find("//") < dotIndex)
        {
            return 0;
        }
        if (line.find("/*") != string::npos && line.find("/*") < dotIndex)
        {
            return 0;
        }
        // still not safe from middle of multy line comments, I need a comment function
        if (line.at(dotIndex - 1) == ' ' || line.at(dotIndex - 1) == tab)
        // assume no weird "a.foo" vs "a .foo"
        {
            return 1;
        }
        int count = 1;
        while (line.find(".") != string::npos)
        {
            count++;
            line = line.substr(line.find(".") + 1);
        }
        return count;
    }
    return 0;
}
