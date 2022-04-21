def extract_quirc_info(quirc_ans):
    """This function extracts the important fields from +QUIRC response"""
    ans_fields = quirc_ans.split(",")
    status = ans_fields[0].split(":")[1].strip().replace('"', '')
    if status != 'closed':
        quirc_info = {
            'curr_size': int(ans_fields[2])
        }
    else:
        quirc_info = {
            'bytes_to_read': int(ans_fields[1]),
            'curr_size': 0
        }
    quirc_info['status'] = status
    return quirc_info


def extract_qiopen_info(qiopen_ans):
    """This function extracts the important fields from +QIOPEN response"""
    ans_fields = qiopen_ans.split(",")
    qiopen_info = {
        'err_code': int(ans_fields[1]),
        'socket_num': int(ans_fields[0].split(":")[1].strip())
    }
    return qiopen_info


def extract_qird_info(qird_ans):
    """This function extracts the important fields from +QIRD response"""
    ans_fields = qird_ans.split(",")
    if len(ans_fields) == 1:
        qird_info = {
            'bytes_read': 0,
            'bytes_in_buf': 0
        }
        pass
    else:
        qird_info = {
            'bytes_read': int(ans_fields[0].split(":")[1].strip()),
            'bytes_in_buf': int(ans_fields[1].strip())
        }
    return qird_info
