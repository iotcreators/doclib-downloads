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


def parse_http_headers(data):
    """This function parses the content length header value and returns the index of the first byte of actual data"""
    lines = data.decode('cp437').split('\n')
    total_length = 0
    byte_count = 0
    for line in lines:
        header_pair = line.rstrip().split(':')
        header_key = header_pair[0].strip()
        if header_key == 'Content-Length':
            total_length = int(header_pair[1].strip())
        byte_count += (len(line) + 1)  # +1 takes into account the \n lost in the split
        if line.rstrip() == '':
            break

    return {
        'total_size': total_length,
        'first_data_byte': byte_count
    }
