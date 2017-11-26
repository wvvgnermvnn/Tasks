# import pandas as pd
# import numpy as np
# data = pd.read_csv('mlcourse_open/data/telecom_churn.csv')
# print(data.describe())

import sys

PARAMS = {'--integer': True,'--boolean': True,'--string': False}

def param_value_or_none(param_name):
    for arg in sys.argv:
        if param_name in arg:
            return arg.split('=')[1]

    return None


def generate_help_message(file_name):
    msg = ''
    for param_name, required in PARAMS.items():
        if not required:
            param_name = '[{}] '.format(param_name)
        msg += param_name + ' '
    msg = 'Use: {fname} {rest_msg}'.format(fname=file_name, rest_msg=msg)
    return msg

class GetOpt:
    def getopt():
        lst = []
        fh = sys.argv[0]

        if len(sys.argv) == 1 or True in ['help' in arg for arg in sys.argv]:
            return generate_help_message(fh)

        for param_name, required in PARAMS.items():
            value = param_value_or_none(param_name)

            if required:
                if value is None:
                    # returns warning about required value
                    return ' '.join([param_name, 'required'])
                lst.append({param_name: value})
            else:
                lst.append({param_name: value})

        return lst


if __name__ == '__main__':
    print(GetOpt.getopt())