# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df


async def ReportAggregator(context: df.DurableOrchestrationContext):
    
    printId = context.get_input()
    logging.info(f"Report aggregator started for {printId}")


main = df.Orchestrator.create(ReportAggregator)