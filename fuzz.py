import json
import zlib
import struct
import subprocess

def modify_abc_with_checksum(input_file, output_file, offset, new_value):
    """
    修改.abc文件的特定偏移位置的值，并重新计算校验和。 
    """
    with open(input_file, 'rb') as f:
        data = bytearray(f.read())

    if offset < 0 or offset >= len(data):
        raise ValueError("Offset is out of bounds for the file size.")
    
    # 修改特定偏移位置的值
    data[offset] = new_value
    
    # 重新计算校验和
    checksum_data = data[12:]
    new_checksum = zlib.adler32(checksum_data) & 0xffffffff
    data[8:12] = struct.pack('<I', new_checksum)

    with open(output_file, 'wb') as f:
        f.write(data)

if __name__ == "__main__":
    input_file = "test.abc"  # 输入文件路径
    output_file = "modified_test.abc"  # 输出文件路径
    new_value = 0x99  # 新值

    with open(f"results_{hex(new_value)}.jsonl", "a", encoding="utf-8") as f:
        for i in range(9999, 19999): # 修改偏移位置范围
            modify_abc_with_checksum(input_file, output_file, i, new_value)
            result = subprocess.run(
                ["bash", "run.sh"],
                capture_output=True,
                text=True
            )
            out = {"idx": i, "error": result.stderr}
            if result.returncode:
                f.write(json.dumps(out, ensure_ascii=False) + "\n")