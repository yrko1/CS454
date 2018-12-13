//
//  main.cpp
//  PowerMeasure
//
//  Created by Bobby Bruce on 20/11/2014.
//  Copyright (c) 2014 Bobby Bruce. All rights reserved.
//

#include <iostream>
#include <stdlib.h>
#include <unistd.h>

#include <IntelPowerGadget/EnergyLib.h>

int main(int argc, const char * argv[]) {
    if(argc != 2){
        std::cout << "Error: Incorrect number of arguments\nUsage: PowerMeasure [terminal command]\nNote:Commands containing whitespace must be surrounded by quotes";
        return EXIT_FAILURE;
    }
    IntelEnergyLibInitialize();
    int numMsrs = 0;
    GetNumMsrs(&numMsrs);
  //  sleep(1);
    ReadSample();
    int status = system(argv[1]);
    ReadSample();
    
    
    for (int j = 0; j < numMsrs; j++) {
        int funcID;
        char szName[1024];
        GetMsrFunc(j, &funcID);
        GetMsrName(j, szName);
        
        // https://software.intel.com/en-us/articles/intel-power-gadget-20
        // Article shows that Processor is total processor energy consumption (IA Energy + GT Energy + Others which may not be measured). 
        if(funcID == MSR_FUNC_POWER && strcmp(szName, "Processor") == 0){
            int nData;
            double data[3];
            GetPowerData(0, j, data, &nData);
            std::cout << data[1];
        }
    }
    printf("\n");
    
    return WEXITSTATUS(status);
}
