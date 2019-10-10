
print ("hellow spyder")
print ("hellow xcode")

import os
import re
import collections

def search_useful_data():
    file_path = os.path.dirname(os.path.realpath(__file__))
    useful_data_label_a = r' /.*/'
    useful_data_label_b = r'.*'
    for root, dirs, files in os.walk(file_path):
        print ("files is",files)
        print (file_path)
        print (dirs)
        test_date = ''
        for files_f in files:
            print ("file_f is",files_f)
            if os.path.splitext(files_f)[1] == '.txt':
               # file_path = os.path.join(root, file)
                print ("file_path is", file_path)

                txt_name = ''.join([os.path.splitext(files_f)[0]+"_generate", '.txt'])
                txt_path = os.path.join(file_path, txt_name)
                log_name=''.join([os.path.splitext(files_f)[0], '.txt'])
                log_path=os.path.join(file_path, log_name)
                print("log_path is :",log_path )
                print("txt_path is :",txt_path )
                print("Start to read file: %s"% file_path )

                with open(txt_path, 'w') as txtfile:
                    with open(log_path, 'rb') as fp:
                        fp_lines = fp.readlines()
                        for line_numb, line_string in enumerate(fp_lines):
                          #  if re.search(useful_data_label_a,line_string):
                            if re.search(useful_data_label_b,line_string):
                            # if re.search(useful_data_label_a, line_string)or(useful_data_label_b,line_string):
                                if re.search(useful_data_label_a,line_string):
                                    line_string_del=line_string
                                    print ("line_string is",line_string)
                                    txtfile.write(line_string)

if "__main__" == __name__:
    search_useful_data()
