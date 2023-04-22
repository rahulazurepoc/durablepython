import logging
import json
import ast 

import azure.functions as func
import azure.durable_functions as df


def ReportGenerator(context: df.DurableOrchestrationContext) -> None:

    current_value = context.get_state(lambda: {"timerInitialized": 0})
    logging.info(f"current value is: {current_value}")

    printId = context.get_input()

    #orchestratorClient = df.DurableOrchestrationClient(oClient)

    operation = context.operation_name
    if operation == "generatereport":
        if current_value["timerInitialized"] == 0 :
            current_value["timerInitialized"] = 1
            context.set_state(current_value)
            logging.info('Initialized timer')

            logging.info(f'calling report aggregator for {printId}')
            

        else:
            logging.info(f'Timer already initialized for {printId}')    
        
    elif operation == "timeout":
        logging.info('15 minute timer expired')
    elif operation == "reportgenerated":
        logging.info('report generated')
    

main = df.Entity.create(ReportGenerator)