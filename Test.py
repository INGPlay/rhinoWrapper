from rhinoWrapper import Rhino

rn = Rhino(filters=["가"], 
           exclude_pos="SN"
           )

text = ["뭐하냐 이놈아 가라"]
pos = ["JKS", "NNG", "NNP", "NNB", "EP", "EF", "NNB", "NP", "VA", "VV", "VX", "XSV", "EC", "VCP", "XR"]
print(rn.wholeResult_list(text, pos = None, filters=None, exclude_pos=None))
print(rn.wholeResult_list(text, pos = None, filters=["이놈아"], exclude_pos=["XR"]))
print(rn.wholeResult_list(text, pos = None, filters="이놈아", exclude_pos="XR"))
print(rn.onlyMorph_list(text, pos = pos, filters=""))
print(rn.onlyMorph_list(text, pos = pos, filters=["뭐"], exclude_pos=["XSV"]))
print(rn.onlyMorph_list(text, pos = pos, filters="뭐", exclude_pos="XSV"))
print(rn.wholeResult_text(text))

text = ["뭐하냐 이놈아 가라", "아나", "이놈아", 1]
pos = ["JKS", "NNG", "NNP", "NNB", "EP", "EF", "NNB", "NP", "VA", "VV", "VX", "XSV", "EC", "VCP", "XR"]
print(rn.wholeResult_list(text, pos = None, filters=None, exclude_pos=None))
print(rn.wholeResult_list(text, pos = None, filters=["이놈아"], exclude_pos=["XR"]))
print(rn.wholeResult_list(text, pos = None, filters="이놈아", exclude_pos="XR"))
print(rn.onlyMorph_list(text, pos = pos, filters=""))
print(rn.onlyMorph_list(text, pos = pos, filters=["뭐"], exclude_pos=["XSV"]))
print(rn.onlyMorph_list(text, pos = pos, filters="뭐", exclude_pos="XSV"))
print(rn.wholeResult_text(text))

