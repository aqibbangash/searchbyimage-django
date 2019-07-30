
class convertIngredients:

    def run(string):
        dict = {}
        list = string.split(',')
        for s in list:
            s = s.split(':')
            dict[s[0].strip()] = s[1].strip()
        return dict


# return example {'Dry Vermouth': '1 part', 'Vodka': '2 parts'}
