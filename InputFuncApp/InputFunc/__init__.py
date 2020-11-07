import logging

import azure.functions as func


def main(req: func.HttpRequest, msg: func.Out[str]) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')

    input_msg = req.params.get('message')

    msg.set(input_msg)

    return 'OK'
