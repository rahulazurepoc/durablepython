import logging
import json

import azure.functions as func
import azure.durable_functions as df

async def main(req: func.HttpRequest, dClient: str) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        reportGeneratorClient = df.DurableOrchestrationClient(dClient)
        entityId = df.EntityId("ReportGenerator", name)
        workflowInputData =  name
        await reportGeneratorClient.signal_entity(entityId, "generatereport",workflowInputData)
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
