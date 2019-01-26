from getPageElement import getContent
import pandas as pd
import xlsxwriter

job_desc = getContent("","")
print(job_desc)

with pd.ExcelWriter('output.xlsx') as writer:
    df = pd.DataFrame({'Data': [job_desc]})
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
