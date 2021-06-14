from PyPDF2 import PdfFileWriter, PdfFileReader
import os



def edit(files=["D:\ht-5.pdf"]):
    for file in files:
        #nameing output file
        head_tail = os.path.split(file)
        x=head_tail[1].split(".")
        x[0]+="edited"
        "".join(x)
        head_tail[1]=x
        "".join(head_tail)


        infile = file

        outfile = head_tail

        page_range = "4-8,6"

        output = PdfFileWriter()
        input_pdf = PdfFileReader(open(infile, "rb"))
        output_file = open(outfile, "wb")


        page_ranges = (x.split("-") for x in page_range.split(","))
        range_list = [i for r in page_ranges for i in range(int(r[0]), int(r[-1]) + 1)]


        for p in range_list:
            # Subtract 1 to deal with 0 index
            output.addPage(input_pdf.getPage(p - 1))
        output.write(output_file)

edit()