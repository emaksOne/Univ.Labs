#include <windows.h>
#include <stdio.h>
#include <tchar.h>
#include <string>
#include <ppl.h>
#include <thread>
#include <future> 

using namespace std;

const string f_procPath = "C:\\leetCode\\volochov_lab2\\Debug\\f_process.exe";
const string g_procPath = "C:\\leetCode\\volochov_lab2\\Debug\\g_process.exe";
bool canExitThread = false;
std::wstring s2ws(const std::string& s)
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

int startProc(string strPath, int arg)
{
	STARTUPINFO si;
	PROCESS_INFORMATION pi;

	ZeroMemory(&si, sizeof(si));
	si.cb = sizeof(si);
	ZeroMemory(&pi, sizeof(pi));


	char text[20];
	itoa(arg, text, 10);
	wchar_t wtext[20];
	mbstowcs(wtext, text, strlen(text) + 1);//Plus null
	LPWSTR ptr = wtext;
	string str = strPath;
	wstring temp = s2ws(str);
	LPCWSTR path = temp.c_str();
	// Start the child process. 
	if (!CreateProcess(path,   // No module name (use command line)
		ptr,        // Command line
		NULL,           // Process handle not inheritable
		NULL,           // Thread handle not inheritable
		FALSE,          // Set handle inheritance to FALSE
		0,              // No creation flags
		NULL,           // Use parent's environment block
		NULL,           // Use parent's starting directory 
		&si,            // Pointer to STARTUPINFO structure
		&pi)           // Pointer to PROCESS_INFORMATION structure
		)
	{
		DWORD error = GetLastError();
		printf("CreateProcess failed (%d).\n", error);
		return -1;
	}
	// Wait until child process exits.
	DWORD val = WaitForSingleObject(pi.hProcess, INFINITE);

	DWORD exitCode;
	GetExitCodeProcess(pi.hProcess, &exitCode);
	return exitCode;
}

void controlThread()
{
	bool continueAndDontAsk = false;
	while (!canExitThread)
	{
		if (!continueAndDontAsk)
		{
			this_thread::sleep_for(chrono::seconds(10));
			
			char input = '\0';
			bool canContinue = false;
			while (true)
			{
				if (canExitThread)
					return;
				printf("Do you want to continue press 'y' if not - press 'n'\n");
				printf("Do you want to continue and don't ask this question again press 'c'\n");
				scanf(" %c", &input);
				if (input == 'c')
				{
					continueAndDontAsk = true;
					break;
				}
				if (input == 'n')
				{
					exit(0);
				}
				if (input == 'y')
				{
					break;
				}
				else
					printf("Unrecognized symbol. Try again...\n");
			}
		}
	}
}


void main(int argc, char *argv[])
{
	//parallel_for()
	int arg = 0;
	printf("Please input x\n");
	scanf("%d", &arg);
	std::future<int> resf =  async(startProc, f_procPath, arg);
	std::future<int> resg = async(startProc, g_procPath, arg);
	thread backThread(controlThread);
	canExitThread = true;
	printf("calculating f(x) and g(x)\n");
	int f = resf.get();
	int g = resg.get();
	

	printf("f(x) = %d\ng(x) = %d\n", f, g);
	printf("f(x) * g(x) = %d * %d = %d\n", f, g, f*g);
	system("PAUSE");
}