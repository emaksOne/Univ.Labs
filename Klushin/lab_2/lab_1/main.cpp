#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <windows.h>
#include <fstream>
#include <string>
#include <sstream>
#include <iterator>
using namespace std;

//map<pair<int, int>, int> hitsToInterval; // #A(i,j) 

//map<pair<int, int>, pair<double, double>> confidenceIntervals; // I(i,j)

//map<tuple<int, int, int>, double> proximityMeasures; // tuple(k, l , i) where k, l - numbers of patients and i - number of column

map<int, double> k1;

map<int, double> k2;

map<int, double> k3;

map<int, double> k4;

class Patient
{
	public:
		int id;
		vector<vector<double>> data;
		Patient()
		{
			
		}

		Patient(vector<vector<double>> mData, int mId)
		{
			data = mData;
			id = mId;
		}

		Patient(int mId)
		{
			Patient();
			id = mId;
			vector<vector<double>> test(15);
			data = test;
		}
};

class Group
{
	public:
		vector<Patient*> pationsList;

		Group()
		{

		}
};

//map<pair<int, int>, int> calculateHitsToIntreval(vector<double> &x, vector<double> &y) // fill #A(i,j)
//{
//	map<pair<int, int>, int> hitsToInterval;   // #A(i,j) 
//	sort(x.begin(), x.end());
//	for (int i = 0; i < x.size(); i++)
//	{
//		for (int j = i + 1; j < x.size(); j++)
//		{
//			for (int k = 0; k < y.size(); k++)
//			{
//				if (y[k] < x[j] && y[k] > x[i])
//				{
//					hitsToInterval[make_pair(i, j)]++;
//				}
//			}
//		}
//	}
//	return hitsToInterval;
//}

double getCustomSqrt(int m, int g, double hij)
{
	double result = hij * (1 - hij) * m + 0.25 * g * g;
	result = sqrt(result);
	return result;
}

double getLeftPointLimitInterval(int m, int g, double hij) // 3d parametr is h(i,j)
{
	double result = (hij * m + 0.5 * g*g - g * getCustomSqrt(m, g, hij)) / (m + g*g);
	return result;
}

double getRightPointLimitInterval(int m, int g, double hij) // 3d parametr is h(i,j)
{
	double result = (hij * m + 0.5 * g*g + g * getCustomSqrt(m, g, hij)) / (m + g*g);
	return result;
}



//map<pair<int, int>, pair<double, double>> calculateConfidenceIntervals(vector<double> &x, vector<double> &y) // fill interval (P(i,j)(1) ; P(i,j)(2))
//{
//	map<pair<int, int>, int> hitsToInterval = calculateHitsToIntreval(x, y); 
//	map<pair<int, int>, pair<double, double>> confidenceIntervals; // I(i,j)
//	int N = y.size();
//	//int N = (x.size() % 2 == 0) ? x.size() / 2 * (x.size() - 1) : (x.size() - 1) / 2 * x.size();
//	for (int i = 0; i < x.size(); i++)
//	{
//		for (int j = i + 1; j < x.size(); j++)
//		{
//			double hij = (double)hitsToInterval[make_pair(i, j)]/N;	
//			double leftPoint = getLeftPointLimitInterval(N, 3, hij);
//			double rightPoint = getRightPointLimitInterval(N, 3, hij);
//			confidenceIntervals[make_pair(i, j)] = make_pair(leftPoint, rightPoint);
//		}
//	}
//	return confidenceIntervals;
//}

int calculateCountOfIntervalsThatContainProbability(vector<double> &x, vector<double> &y) // #B(i,j)
{
	//map<pair<int, int>, int> hitsToInterval = calculateHitsToIntreval(x, y);
	sort(x.begin(), x.end());
	int hitsToInterval = 0;
	int count = 0;
	int N = y.size();
	for (int i = 0; i < x.size(); i++)
	{
		for (int j = i + 1; j < x.size(); j++)
		{
			for (int k = 0; k < y.size(); k++)
			{
				if (y[k] < x[j] && y[k] > x[i])
				{
					hitsToInterval++;
				}
			}
			double probability = (double)(j - i) / (x.size() + 1);
			//double hij = (double)hitsToInterval[make_pair(i, j)] / N;
			double hij = (double)hitsToInterval / N;
			double leftPoint = getLeftPointLimitInterval(N, 3, hij);
			double rightPoint = getRightPointLimitInterval(N, 3, hij);
			if (probability < rightPoint && probability > leftPoint)
			{
				count++;
			}
			hitsToInterval = 0;
		}

	}
	return count;
}

double getProximityMeasure(vector<double> &x, vector<double> &y) // ro(X,Y)
{
	int count = calculateCountOfIntervalsThatContainProbability(x, y);
	int N = (x.size() % 2 == 0) ? x.size() / 2 * (x.size() - 1) : (x.size() - 1) / 2 * x.size();
	double result = (double)count / N;
	return result;
}


double getAverageProximityMeasureForKthPatientForIColumn (Group *group, int k, int i) // in the same group
{
	if (k > group->pationsList.size())
	{
		cout << "Error: k is bigger than size of vector";
		return 0;
	}
	double count = 0;
	for (int l = 0; l < group->pationsList.size(); l++)
	{
		if (l != k)
		{
			//double ro = getProximityMeasure(group->pationsList[k]->data[i], group->pationsList[l]->data[i]);
			double ro1 = getProximityMeasure(group->pationsList[k]->data[i], group->pationsList[l]->data[i]);
			double ro2 = getProximityMeasure(group->pationsList[l]->data[i], group->pationsList[k]->data[i]);
			//count += ro;
			count += (ro1 + ro2) * 0.5;
		}
	}
	double result = 1.0 / (group->pationsList.size() - 1) * count;
	return result;
}

double getAverageProximityMeasureForKthPatientForIColumn(Group *group1, Group *group2, int k, int i) // in the different groups
{
	if (k > group1->pationsList.size())
	{
		cout << "Error: k is bigger than size of vector";
		return 0;
	}
	double count = 0;
	for (int l = 0; l < group2->pationsList.size(); l++)
	{
		//double ro = getProximityMeasure(group1->pationsList[k]->data[i], group2->pationsList[l]->data[i]);
		double ro1 = getProximityMeasure(group1->pationsList[k]->data[i], group2->pationsList[l]->data[i]);
		double ro2 = getProximityMeasure(group2->pationsList[l]->data[i], group1->pationsList[k]->data[i]);
		//count += ro;
		count += (ro1 + ro2) * 0.5;
	}
	double result = 1.0 / (group2->pationsList.size()) * count;
	return result;
}

double getAverageAverageProximityMeasureForIColumn(Group *group, int i) // in the same group   ( K1(i))
{
	double count = 0;
	for (int k = 0; k < group->pationsList.size(); k++)
	{
		double temp = getAverageProximityMeasureForKthPatientForIColumn(group, k, i);
		count += temp;
	}
	double result = 1.0 / (group->pationsList.size()) * count;
	return result;
}

double getAverageAverageProximityMeasureForIColumn(Group *group1, Group *group2, int i) // in the same group   ( K2(i))
{
	double count = 0;
	for (int k = 0; k < group1->pationsList.size(); k++)
	{
		double temp = getAverageProximityMeasureForKthPatientForIColumn(group1, group2, k, i);
		count += temp;
	}
	double result = 1.0 / (group1->pationsList.size()) * count;
	return result;
}




void calculateStatistics(Group *group1, Group *group2)
{
	printf("  (X,Y)\t\t\t(X,X)\t\t\t(Y,X)\t\t\t(Y,Y)\n\n");
	for (int i = 0; i < 15; i++)
	{
		k1[i] = getAverageAverageProximityMeasureForIColumn(group1, group2, i);
		printf("k1[%d] = %f   ", i, k1[i]);
		k2[i] = getAverageAverageProximityMeasureForIColumn(group1, i);
		printf("k2[%d] = %f   ", i, k2[i]);
		k3[i] = getAverageAverageProximityMeasureForIColumn(group2, group1, i);
		printf("k3[%d] = %f   ", i, k3[i]);
		k4[i] = getAverageAverageProximityMeasureForIColumn(group2, i);
		printf("k4[%d] = %f\n", i, k4[i]);
	}
}

wstring s2ws(const string& s)
{
	int len;
	int slength = (int)s.length() + 1;
	len = MultiByteToWideChar(CP_ACP, 0, s.c_str(), slength, 0, 0);
	wchar_t* buf = new wchar_t[len];
	MultiByteToWideChar(CP_ACP, 0, s.c_str(), slength, buf, len);
	std::wstring r(buf);
	delete[] buf;
	return r;
}

vector<string> getFiles(string directory)
{
	vector<string> files;
	WIN32_FIND_DATA fd;


	string path = directory + "/*.POK";

	HANDLE h = FindFirstFile(s2ws(path).c_str(), &fd);
	if (h != INVALID_HANDLE_VALUE) {
		do {

			wstring ws(fd.cFileName);
			string name(ws.begin(), ws.end());
			files.push_back(name); 

		} while (FindNextFile(h, &fd));
			FindClose(h);
	}

	return files;
}

vector<string> splitString(string line)
{
	vector<string> tokens;
	istringstream iss(line);
	copy(istream_iterator<string>(iss),
		istream_iterator<string>(),
		back_inserter(tokens));
	return tokens;
}

void addToPatient(Patient *patient, string line)
{
	vector<string> data = splitString(line); 
	if (data.size() < 15)
		return;
	for (int i = 0; i < patient->data.size(); i++)
	{
		double temp = stod(data[i + 1]);
		patient->data[i].push_back(temp); 
	}
}

void readInGroup(string directory, Group* group)
{
	vector<string> files = getFiles(directory);
	for (int i = 0; i < files.size(); i++)
	{
		Patient *patient = new Patient(i);
		string line;
		string path = directory + '/' + files[i];
		ifstream myfile(path);
			
		if (myfile.is_open())
		{
			while (getline(myfile, line))
			{
				addToPatient(patient, line);
			}
			myfile.close();
		}
		group->pationsList.push_back(patient);
	}
	
}

void writeToFile()
{
	FILE * pFile;
	pFile = fopen("results.txt", "w");
	fprintf(pFile, "(X,Y)\t\t\t(X,X)\t\t\t(Y,X)\t\t\t(Y,Y)\n");
	for (int i = 0; i < k1.size(); i++)
	{
		fprintf(pFile, "k1[%d] = %f\tk2[%d] = %f\tk3[%d] = %f\tk4[%d] = %f\n\n", i,k1[i],i,k2[2],i,k3[i],i,k4[i]);
	}
	fclose(pFile);

}


int main()
{
	
	Group *group1 = new Group();
	Group *group2 = new Group(); 
	readInGroup("ALLD2", group1);
	readInGroup("ALLD3", group2);

	calculateStatistics(group1, group2);
	writeToFile();

	system("PAUSE");
}

