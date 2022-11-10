n = [[0.775, 0.9205882352941176, 0.9748447204968944],
 [0.775, 0.396808510638298, 0.6973309608540926],
 [0.775, 0.9205882352941176],
 [0.775,
  0.9205882352941176,
  0.9748447204968944,
  0.9923246999368289,
  0.9976855673376088,
  0.9993045972260203]]


for score_list_idx, score_list in enumerate(n):
    can_pass = False
    for score_idx, score in enumerate(score_list):
        if score_idx-1 == len(score_list):
            print(f'kc_index: {score_list_idx} never mastered.')
        if can_pass:
            continue
        if score > 0.950:
            print(f'score: {score} - fdx: {score_idx} | kc_index: {score_list_idx}')
            can_pass = True

print('test')
