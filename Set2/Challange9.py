def pkcs7_pad(msg, blk):
    pad_len = blk - (len(msg)%blk)
    return msg + bytes([pad_len])*pad_len

def main():
    buffer = bytearray("YELLOW SUBMARINE", 'utf-8')
    blk_size = 20
    print(pkcs7_pad(buffer, blk_size))
                       
main()
