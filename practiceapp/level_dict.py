# 递归显示关联数组的key
def show_level_dict(target_dict):
    if isinstance(target_dict, dict):
        for k in target_dict:
            print(k)
            show_level_dict(target_dict[k])


mydict = {'country': {'capital': 'biejing', 'info': {'populator': '14billon'}, 'flower': 'egggflower'}}

show_level_dict(mydict)
