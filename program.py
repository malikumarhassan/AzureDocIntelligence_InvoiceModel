from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient


# declare endpoint, key and invoice document URL, here I am using public URL of document you can use local path as well
endpoint = "**************************************************************"
key =  "*****************************************************************"
ducumentURL = "https://idodata.com/wp-content/uploads/2024/02/Adatum-1.pdf"

# declare document analysis variable 
document_analysis_document = DocumentAnalysisClient(
                            endpoint= endpoint,
                            credential= AzureKeyCredential(key))

# here begin_analyze_document_from_url is used to analysize the pdf , if you want to read from local directory used "begin_analyze_document",
# first parameter is model name and second is document url
pollar = document_analysis_document.begin_analyze_document_from_url("prebuilt-invoice", ducumentURL)
result = pollar.result()


''' Extract Key Value Pair from inovice.  first we going to print all fields value from the document
then we are checking data type string then print the field value. thrid if you need to print only particular
field e.g. Customer name you can also print.
'''
for document in result.documents:
    print("Print Document")
    for field in document.fields:
        # print all fields of document
        print(f"Field  {field} - {document.fields[field].value} ")

        #print only string data type of document
        if document.fields[field].value_type ==  "string":           
            print(f"{field} : {document.fields[field].value}")
    # get only Customer Name filed
    fieldvalue = document.fields.get("CustomerName")
    if fieldvalue:   
        print("--------------Print only customer name---------------")
        print(f"Customer Name {fieldvalue.value}")

print("-----------")





''' First extract no. of rows and columns from the table 
and align in to table format
'''
for table in result.tables:
    print(f"Table has {table.row_count} rows and {table.column_count} columns")
    linenumnber = 0
    for cell in table.cells:
        rowindex =  cell.row_index
        if rowindex != linenumnber:
            linenumnber = rowindex
            print("")
        # extracting cell content of table 
        print(f"{cell.content}", end="")