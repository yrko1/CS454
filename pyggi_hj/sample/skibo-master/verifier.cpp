
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <IntelPowerGadget.framework/Heaeders/EnergyLib.h>

int main(int argc, char* argv[]) {

	IntelEnergyLibInitialize();
	StartLog("/tmp/PowerGadgetLog.csv"); // causes a sample to be read
	
	int numMsrs = 0;
	GetNumMsrs(&numMsrs);
	
	for (int i = 0; i < 10; i++) {
		
		sleep(1);
		ReadSample();
		
		for (int j = 0; j < numMsrs; j++) {
			int funcID;
			char szName[1024];
			GetMsrFunc(j, &funcID);
			GetMsrName(j, szName);
			
			int nData;
			double data[3];
			GetPowerData(0, j, data, &nData);
			
			// Frequency
			if (funcID == MSR_FUNC_FREQ) {
				printf("%s = %4.0f", szName, data[0]);
			}
			
			// Power
			else if (funcID == MSR_FUNC_POWER) {
				printf(", %s Power (W) = %3.2f", szName, data[0]);
				printf(", %s Energy(J) = %3.2f", szName, data[1]);
				printf(", %s Energy(mWh)=%3.2f", szName, data[2]);
			}
			
			// Temperature
			else if (funcID == MSR_FUNC_TEMP) {
				printf(", %s Temp (C) = %3.0f", szName, data[0]);
			}
		}
		printf("\n");
	}
	
	sleep(1);
	StopLog();// causes a sample to be read
	
	return 0;
}

