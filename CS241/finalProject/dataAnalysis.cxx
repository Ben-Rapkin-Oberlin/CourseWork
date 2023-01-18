//Coded by Hikari


//aproximate time spent: >28 hours

//known bug where program will run forever if none of the training data set for a person has a value for one of the data points
//this is a fringe case and should never happen under normal operation, any data set we plan to use the program with should have at least 1 value for each data point

//known bug where program crashes upon bootstrap returning the array to dataAnalysis/when the return value is used.
//Originally thought that this was due to being unable to return a std::array created in the scope of bootstrap, so I rewrote bootstrap to take and return a pointer to a float array instead.
//unfortunately this did not work, and googling didn't show anyone else with the same problem

#include <vector>
#include <filesystem>
#include <string>
#include <utility>
#include <random>
#include <array>
#include <cmath>




using namespace std;

array<float, 10> train(string a); //prototype


//bootstraps randomly sampling the vector data set to create bCount samples, returns array pointer given in input with updated info
//return array is structured SD 0, Mean 0, SD 1, Mean 1, etc. 
float* bootstrap(std::vector<std::array<float, 10> > data, int bCount, float * fData) {
	
	//device generates random seed for number generator
	std::random_device rd;

	//mersenne twister random number generator for bootstrap
	std::mt19937 gen(rd());

	//filters rng to be uniformly distibuted data element indices for random sampling
	std::uniform_int_distribution<int> dist(0, data.size() -1);

	std::vector<float * > bData; //create temp vector for bootstrap data, stores pointers to float arrays

	float gen0, gen1, gen2, gen3, gen4, gen5, gen6, gen7, gen8, gen9; //temporarily stores float values for filling bootstrap samples

	//creates new data samples equal to bCount, stores in bData
	for (int i = 0; i < bCount; ++i) {

		//fills array datapoints with randomly selected nonzero datapoint (train returns zero if it fails to find that piece of data)
		gen0 = data.at(dist(gen))[0];
		while (gen0 == 0) {
			gen0 = data.at(dist(gen))[0];
		}
		gen1 = data.at(dist(gen))[1];
		while (gen1 == 0) {
			gen1 = data.at(dist(gen))[1];
		}
		gen2 = data.at(dist(gen))[2];
		while (gen2 == 0) {
			gen2 = data.at(dist(gen))[2];
		}
		gen3 = data.at(dist(gen))[3];
		while (gen3 == 0) {
			gen0 = data.at(dist(gen))[3];
		}
		gen4 = data.at(dist(gen))[4];
		while (gen4 == 0) {
			gen4 = data.at(dist(gen))[4];
		}
		gen5 = data.at(dist(gen))[5];
		while (gen5 == 0) {
			gen5 = data.at(dist(gen))[5];
		}
		gen6 = data.at(dist(gen))[6];
		while (gen6 == 0) {
			gen6 = data.at(dist(gen))[6];
		}
		gen7 = data.at(dist(gen))[7];
		while (gen7 == 0) {
			gen7 = data.at(dist(gen))[7];
		}
		gen8 = data.at(dist(gen))[8];
		while (gen8 == 0) {
			gen8 = data.at(dist(gen))[8];
		}
		gen9 = data.at(dist(gen))[9];
		while (gen9 == 0) {
			gen9 = data.at(dist(gen))[9];
		}

		//creates new dynamically allocated array stored in vector at index
		bData.push_back(new float[10]{
			//populates array by sampling with replacement from data set. This means that the array is a randomly generated new data piece that can be used for statistical analysis.
			gen0,
			gen1,
			gen2,
			gen3,
			gen4,
			gen5,
			gen6,
			gen7,
			gen8,
			gen9
			});
	}

	//temp variable for adding all values to find mean and adding values to find standard deviation
	float tempSum;



	int i, x; //variables for loops

	for (i = 0; i < 10; ++i) {

		tempSum = 0;

		//loops through each sample to add for mean
		for (x = 0; x < bCount; ++x) {
			tempSum += bData.at(x)[i];
		}
		tempSum = tempSum / bCount;
		//inserts mean at correct position in fData
		fData[(i * 2) +1] = tempSum;

		tempSum = 0;

		//loops through each sample to add for SD according to formula for standard deviation
		for (x = 0; x < bCount; ++x) {
			tempSum = tempSum + std::pow(std::abs(bData.at(x)[i]/*value*/ - fData[(i * 2) +1 ] /*mean*/), 2);
		}
		//finishes calulating SD and places it in correct position in fData
		fData[i*2] = std::sqrt(tempSum / bCount);
	}

	//cleans up
	for (x = 0; x < bCount; ++x) {
		delete[] bData.at(x);
	}
	bData.~vector();
	return fData;
}

//takes path for data directory to analyize and number of samples to bootstrap as input
//outputs pair of vectors, first is a list of names, and second is a list of data statistics
//index of data statistics for a person corresponds to the index of that person's name in the name list
//data statistics are structed as an vector of float array pointers, which each float array being structed as follows: SD 0, Mean 0, SD 1, Mean 1, ... SD 9, Mean 9
//note that the arrays are not null terminated, but are all size 20

std::pair< std::vector<string>, std::vector<float * > > dataAnalysis(string path, int bootCount) {
	std::vector<float *> pData;
	std::vector<string> pNames; //index of name list correlates to index in pData with that person's data




	//loops through main directory of people
	for (const auto& person : std::filesystem::directory_iterator(path)) {
		pNames.push_back(person.path().stem().string()); //adds to name list
		std::vector<std::array<float, 10> > tempData; //create temp vector for person's code




		//loops through a person's code directory
		for (const auto& file : std::filesystem::directory_iterator(person.path())) {
			tempData.push_back(train(file.path().string()));
			//tempData.push_back(std::array<float, 10> {1, 1, 2, 3, 4, 5, 6, 7, 8, 9}); //placeholder values for testing without calling train
		}

		pData.push_back(bootstrap(tempData, bootCount, new float[20]));

		//cleans up
		tempData.~vector();
	}

	//array for return
	std::pair< std::vector<string>, std::vector<float * > > fPair;
	fPair.first = pNames;
	fPair.second = pData;

	return fPair;

}
