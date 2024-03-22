import logging
import os.path

import os

from adobe.pdfservices.operation.auth.credentials import Credentials
from adobe.pdfservices.operation.client_config import ClientConfig
from adobe.pdfservices.operation.exception.exceptions import ServiceApiException, ServiceUsageException, SdkException
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_pdf_options import ExtractPDFOptions
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_element_type import ExtractElementType
from adobe.pdfservices.operation.execution_context import ExecutionContext
from adobe.pdfservices.operation.io.file_ref import FileRef
from adobe.pdfservices.operation.pdfops.extract_pdf_operation import ExtractPDFOperation

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

base_path= os.getcwd()
# get base path.
pdf_folder_name="/2022_river_pdfs/"
folder_path = base_path+ pdf_folder_name
# List all files in the folder
files = os.listdir(folder_path)

credentials = Credentials.service_principal_credentials_builder(). \
        with_client_id("-YOUR CLIENT ID-"). \
        with_client_secret("YOUR CLIENT SECRET"). \
        build()
 # Create client config instance with custom time-outs.
client_config = ClientConfig.builder().with_connect_timeout(10000)\
        .with_read_timeout(40000)\
        .with_processing_timeout(700000)\
        .build()

failed_pdf=[]
def get_excell(file_name):
    try:
        # Create an ExecutionContext using credentials and create a new operat,cion instance.
        execution_context = ExecutionContext.create(credentials,client_config)
        extract_pdf_operation = ExtractPDFOperation.create_new()
        source = FileRef.create_from_local_file(base_path +pdf_folder_name+file_name)
        extract_pdf_operation.set_input(source)

        # Build ExtractPDF options and set them into the operation
        extract_pdf_options: ExtractPDFOptions = ExtractPDFOptions.builder() \
            .with_element_to_extract(ExtractElementType.TEXT) \
            .with_element_to_extract(ExtractElementType.TABLES) \
            .build()
        extract_pdf_operation.set_options(extract_pdf_options)

        # Execute the operation.
        result: FileRef = extract_pdf_operation.execute(execution_context)

        # Save the result to the specified location.
        output_path=base_path + "/output_2022_rivers/"+file_name.split(".")[0]+".zip"
        result.save_as(output_path)
        return output_path
        
    except (ServiceApiException, ServiceUsageException, SdkException):
        logging.exception("Exception encountered while executing operation")
        failed_pdf.append(file_name)
        return None


def __main__():
    if __name__ == "__main__":
        # Your main code here
        for file in files:
            get_excell(file)
        print("Main function in Python")
        for file in failed_pdf:
            print(file)
      

# Call the main function
__main__()
